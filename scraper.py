import re
from io import StringIO

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Faizur Financial Research contact@example.com"}

# Multiplier to normalize every extracted figure to millions, based on the
# "(In millions...)" / "(In thousands...)" caption found near the table.
UNIT_MULTIPLIERS = {
    "in billions": 1000.0,
    "in thousands": 0.001,
    "in millions": 1.0,
}

# Real captions/headings that identify a statement, as opposed to guessing
# from row labels alone (which is what let MD&A / segment tables get
# mistaken for the real statement before).
STATEMENT_TITLE_HINTS = {
    "income": [
        "statements of operations", "statement of operations",
        "statements of income", "statement of income",
    ],
    "balance": [
        "balance sheets", "balance sheet", "statements of financial position",
    ],
    "cashflow": [
        "statements of cash flows", "statement of cash flows",
    ],
}


def download_filing(url):
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.text


def normalize(text):
    return str(text).lower().replace("\n", " ").replace("\xa0", " ").strip()


def clean_dataframe(df):
    df = df.replace(r'^\s*$', np.nan, regex=True)
    df = df.dropna(how='all', axis=0).dropna(how='all', axis=1)
    return df.reset_index(drop=True)


def _nearby_context(table_tag, max_chars=600, max_prev_nodes=6):
    """Collect the text immediately preceding a table in the document, e.g.
    'CONSOLIDATED STATEMENTS OF OPERATIONS' or '(In millions, except per
    share amounts)'. pd.read_html alone throws this context away, which is
    why the old code had to guess a table's identity from its row labels."""
    chunks = []
    node = table_tag
    seen = 0
    while node is not None and seen < max_prev_nodes:
        node = node.find_previous(string=True)
        if node is None:
            break
        text = node.strip() if isinstance(node, str) else ""
        if text:
            chunks.append(text)
            seen += 1
    context = " | ".join(reversed(chunks))
    return normalize(context)[:max_chars]


def extract_tables_with_context(html):
    """Returns a list of (dataframe, nearby_context_text) tuples."""
    soup = BeautifulSoup(html, "lxml")
    results = []
    for table_tag in soup.find_all("table"):
        try:
            dfs = pd.read_html(StringIO(str(table_tag)), flavor="lxml")
        except ValueError:
            continue
        if not dfs:
            continue
        df = clean_dataframe(dfs[0])
        if df.shape[0] > 3 and df.shape[1] > 1:
            context = _nearby_context(table_tag)
            results.append((df, context))
    return results


def _unit_multiplier(context):
    for phrase, mult in UNIT_MULTIPLIERS.items():
        if phrase in context:
            return mult
    return 1.0


def parse_numeric_cell(text):
    text_norm = normalize(text)
    # FIX: was "(:\.\d+)?" (a literal, near-impossible-to-match colon)
    # instead of a non-capturing decimal group.
    match = re.search(r"\(?([\d,]+(?:\.\d+)?)\)?", text_norm)
    if not match:
        return None
    clean_num = match.group(1).replace(",", "")
    try:
        value = float(clean_num)
    except ValueError:
        return None
    if "(" in text_norm or "\u2013" in text_norm or text_norm.strip().startswith("-"):
        value *= -1
    return value


def find_primary_statement(tables_with_context, primary_keywords, supporting_keywords, statement_kind):
    """tables_with_context: list of (df, context) tuples from extract_tables_with_context."""
    title_hints = STATEMENT_TITLE_HINTS[statement_kind]
    best = None
    max_score = -1

    for df, context in tables_with_context:
        labels = []
        for _, row in df.iterrows():
            lbl = normalize(" ".join(str(x) for x in row.values[:2] if pd.notna(x)))
            labels.append(lbl)
        full_labels_str = " ".join(labels)

        has_primary = any(kw in full_labels_str for kw in primary_keywords)
        has_supporting = any(kw in full_labels_str for kw in supporting_keywords)
        if not (has_primary and has_supporting):
            continue

        score = 100
        title_match = any(hint in context for hint in title_hints)
        if title_match:
            # This is the strongest signal available: the table actually sits
            # under a real "CONSOLIDATED STATEMENTS OF ..." caption.
            score += 200
        if df.shape[0] < 10:
            score -= 50
        if "segment" in context and not title_match:
            # Segment/MD&A tables often contain "total revenue" +
            # "operating income" too -- don't let them win without a real
            # statement caption backing them up.
            score -= 150

        if score > max_score:
            max_score = score
            best = (df, context)

    return best


LABEL_PRIORITY_TARGETS = {
    "revenue": [
    "total net sales",
    "net sales",
    "total revenue",
    "total revenues",
    "revenue"
],
    "net_income": [
    "net income",
    "net earnings",
    "income attributable to common shareholders",
    "profit"
],
    "total_assets": ["total assets"],
    "total_liabilities": ["total liabilities"],
    "operating_cash_flow": [
        "net cash provided by operating activities",
        "net cash from operating activities",
        "net cash provided by (used in) operating activities",
        "cash provided by operating activities",
    ],
}

# Row-label endings that must never be treated as the consolidated total,
# even though they technically contain the target word (e.g. "Cloud
# services revenue" ends with "revenue" but is a segment line, not the
# consolidated total). This is the main fix for the wrong Revenue values.
BAD_SUFFIXES = {
    "revenue": [
        "segment revenue", "product revenue", "products revenue", "services revenue",
        "cloud revenue", "cloud services revenue", "devices revenue", "subscription revenue",
    ],
}


def _label_match_rank(label, targets, bad_suffixes):
    """Lower rank = more specific / trustworthy match. None = no match.
    Exact-equality matches always outrank endswith matches, and priority
    follows the order of `targets` (most specific phrase first)."""
    if not label:
        return None
    for suffix in bad_suffixes:
        if label.endswith(suffix):
            return None
    for rank, target in enumerate(targets):
        if label == target:
            return rank
    for rank, target in enumerate(targets):
        if label.endswith(" " + target):
            return rank + len(targets)
    return None


def extract_strict_value(table_with_context, field_key, target_year):
    if table_with_context is None:
        return None
    df, context = table_with_context
    targets = LABEL_PRIORITY_TARGETS[field_key]
    bad_suffixes = BAD_SUFFIXES.get(field_key, [])

    col_year_map = {}
    for _, row in df.head(10).iterrows():
        for col_idx, cell in enumerate(row.values):
            cell_clean = normalize(cell)
            years = re.findall(r"\b(202[0-6])\b", cell_clean)
            for y in years:
                if col_idx not in col_year_map:
                    col_year_map[col_idx] = int(y)

    # FIX: previously this returned on the FIRST row in table order that
    # matched *any* target -- so a segment/product breakdown row listed
    # above the real "Total revenue" line would win. Now every row is
    # scored and the most specific/exact match wins, regardless of order.
    best_row = None
    best_rank = None
    for _, row in df.iterrows():
        lbl1 = normalize(row.values[0]) if pd.notna(row.values[0]) else ""
        lbl2 = normalize(row.values[1]) if pd.notna(row.values[1]) else ""
        rank1 = _label_match_rank(lbl1, targets, bad_suffixes)
        rank2 = _label_match_rank(lbl2, targets, bad_suffixes)
        candidates = [r for r in (rank1, rank2) if r is not None]
        if not candidates:
            continue
        rank = min(candidates)
        if best_rank is None or rank < best_rank:
            best_rank = rank
            best_row = row

    if best_row is None:
        return None

    row_values = []
    for col_idx, cell in enumerate(best_row.values):
        if pd.isna(cell):
            continue
        val = parse_numeric_cell(str(cell))
        if val is not None and not (2020 <= abs(val) <= 2026):
            row_values.append((col_idx, val))

    if not row_values:
        return None

    value = None
    for col_idx, val in row_values:
        if col_year_map.get(col_idx) == target_year:
            value = val
            break

    if value is None:
        row_values.sort(key=lambda x: x[0])
        years_found = list(set(col_year_map.values()))
        max_year = max(years_found) if years_found else target_year
        if target_year == max_year:
            value = row_values[0][1]
        elif len(row_values) > 1 and target_year == (max_year - 1):
            value = row_values[1][1]
        elif len(row_values) > 2 and target_year == (max_year - 2):
            value = row_values[2][1]

    if value is None:
        return None

    return value * _unit_multiplier(context)


def scrape_filing(url, target_year):
    html = download_filing(url)
    tables_with_context = extract_tables_with_context(html)

    income = find_primary_statement(
        tables_with_context,
        ["total revenue", "net sales", "total net sales", "total revenues"],
        ["net income", "net earnings", "operating income"],
        "income",
    )
    balance = find_primary_statement(
        tables_with_context,
        ["total assets", "assets total"],
        ["total liabilities", "retained earnings", "stockholders"],
        "balance",
    )
    cashflow = find_primary_statement(
        tables_with_context,
        ["net cash provided by operating activities", "net cash from operating activities",
         "cash provided by operating activities", "net cash provided by (used in) operating activities"],
        ["investing activities", "financing activities", "free cash flow"],
        "cashflow",
    )

    return {
        "Revenue": extract_strict_value(income, "revenue", target_year),
        "Net Income": extract_strict_value(income, "net_income", target_year),
        "Total Assets": extract_strict_value(balance, "total_assets", target_year),
        "Total Liabilities": extract_strict_value(balance, "total_liabilities", target_year),
        "Operating Cash Flow": extract_strict_value(cashflow, "operating_cash_flow", target_year),
    }