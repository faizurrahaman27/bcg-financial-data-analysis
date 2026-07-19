import requests
import pandas as pd
from bs4 import BeautifulSoup

# ==========================================================
# Configuration
# ==========================================================

URL = "https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/msft-20230630.htm"

HEADERS = {
    "User-Agent": "BCG Task Project (your_email@example.com)"
}

# ==========================================================
# Download 10-K Filing
# ==========================================================

response = requests.get(URL, headers=HEADERS)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

# ==========================================================
# Read all HTML tables
# ==========================================================

all_tables = []

for table in soup.find_all("table"):
    try:
        df = pd.read_html(str(table))[0]
        all_tables.append(df)
    except Exception:
        continue

print(f"\nFound {len(all_tables)} readable tables.\n")

# ==========================================================
# Locate Financial Statements
# ==========================================================

income_df = None
balance_df = None
cashflow_df = None

for df in all_tables:

    text = df.astype(str).to_string().lower()

    if income_df is None:
        if "total revenue" in text and "net income" in text:
            income_df = df

    if balance_df is None:
        if "total assets" in text and "total liabilities" in text:
            balance_df = df

    if cashflow_df is None:
        if (
            "net cash from operations" in text
            or "cash provided by operating activities" in text
            or "cash flows from operating activities" in text
            or "operating activities" in text
        ):
            cashflow_df = df

print("Income Statement Found :", income_df is not None)
print("Balance Sheet Found    :", balance_df is not None)
print("Cash Flow Found        :", cashflow_df is not None)

# ==========================================================
# Function to Extract Financial Metrics
# ==========================================================

def extract_metric(df, keywords, year_column=3):

    if df is None:
        return None

    if isinstance(keywords, str):
        keywords = [keywords]

    labels = (
        df.iloc[:, 0]
        .fillna("")
        .astype(str)
        .str.strip()
        .str.lower()
    )

    for keyword in keywords:

        rows = df[
            labels == keyword.lower()
        ]

        if not rows.empty:
            value = rows.iloc[0, year_column]
            return pd.to_numeric(value, errors="coerce")

    return None
# ==========================================================
# Extract Financial Metrics
# ==========================================================

financials = {

    "Revenue": extract_metric(
        income_df,
        ["Total revenue", "Net sales"]
    ),

    "Net Income": extract_metric(
        income_df,
        "Net income"
    ),

    "Total Assets": extract_metric(
        balance_df,
        "Total assets"
    ),

    "Total Liabilities": extract_metric(
        balance_df,
        "Total liabilities"
    ),

    "Operating Cash Flow": extract_metric(
        cashflow_df,
        [
            "Net cash from operations",
            "Net cash provided by operating activities",
            "Cash provided by operating activities"
        ]
    )
}

# ==========================================================
# Display Results
# ==========================================================

print("\nMicrosoft Financial Data (2023)\n")

for metric, value in financials.items():
    print(f"{metric:<25}: {value}")


print("Cash Flow Found :", cashflow_df is not None)
print(cashflow_df.head(35).to_string())

row = cashflow_df[
    cashflow_df.iloc[:, 0].astype(str).str.contains("Net cash from operations", case=False, na=False)
].iloc[0]

print(row.tolist())