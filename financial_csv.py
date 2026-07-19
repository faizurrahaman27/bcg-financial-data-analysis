import pandas as pd

COLUMN_ORDER = ["Company", "Year", "Revenue", "Net Income", "Total Assets",
                "Total Liabilities", "Operating Cash Flow"]


def _sanity_check(df):
    """Print soft warnings for rows that look implausible so a human can
    spot-check the scrape. This never modifies the data -- it only flags it."""
    for _, row in df.iterrows():
        label = f"{row['Company']} {row['Year']}"

        assets, liabilities = row.get("Total Assets"), row.get("Total Liabilities")
        if pd.notna(assets) and pd.notna(liabilities) and liabilities > assets:
            print(f"  CHECK: {label} - liabilities exceed assets")

        revenue, net_income = row.get("Revenue"), row.get("Net Income")
        if pd.notna(revenue) and pd.notna(net_income) and abs(net_income) > abs(revenue):
            print(f"  CHECK: {label} - net income exceeds revenue")

        for col in COLUMN_ORDER[2:]:
            if pd.isna(row.get(col)):
                print(f"  CHECK: {label} - missing {col}")


def export_to_csv(records, filename):
    df = pd.DataFrame(records)
    for col in COLUMN_ORDER:
        if col not in df.columns:
            df[col] = None
    df = df[COLUMN_ORDER]
    df = df.sort_values(["Company", "Year"]).reset_index(drop=True)

    numeric_cols = COLUMN_ORDER[2:]
    df[numeric_cols] = df[numeric_cols].round(1)

    _sanity_check(df)

    df.to_csv(filename, index=False)
    return df