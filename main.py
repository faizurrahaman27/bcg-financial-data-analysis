from scraper import scrape_filing
from financial_csv import export_to_csv

# NOTE: kept the corrected Tesla accession numbers/URLs (10-K filings, not the
# 10-K/A) -- the originals in main.py were malformed / pointed at an amendment.
FILINGS = {
    "Microsoft": {
        2023: "https://www.sec.gov/Archives/edgar/data/789019/000095017023035122/msft-20230630.htm",
        2024: "https://www.sec.gov/Archives/edgar/data/789019/000095017024087843/msft-20240630.htm",
        2025: "https://www.sec.gov/Archives/edgar/data/789019/000095017025100235/msft-20250630.htm",
    },
    "Apple": {
        2023: "https://www.sec.gov/Archives/edgar/data/320193/000032019323000106/aapl-20230930.htm",
        2024: "https://www.sec.gov/Archives/edgar/data/320193/000032019324000123/aapl-20240928.htm",
        2025: "https://www.sec.gov/Archives/edgar/data/320193/000032019325000079/aapl-20250927.htm",
    },
    "Tesla": {
        2023: "https://www.sec.gov/Archives/edgar/data/1318605/000162828024002390/tsla-20231231.htm",
        2024: "https://www.sec.gov/Archives/edgar/data/1318605/000162828025003063/tsla-20241231.htm",
        2025: "https://www.sec.gov/Archives/edgar/data/1318605/000162828026003952/tsla-20251231.htm",
    },
}

REQUIRED_FIELDS = ["Revenue", "Net Income", "Total Assets", "Total Liabilities", "Operating Cash Flow"]


def main():
    records = []
    for company, years in FILINGS.items():
        for year, url in sorted(years.items()):
            print(f"Processing {company} {year}...")
            try:
                financials = scrape_filing(url, year)
            except Exception as e:
                print(f"  ERROR: {e}")
                financials = {field: None for field in REQUIRED_FIELDS}

            missing = [f for f in REQUIRED_FIELDS if financials.get(f) is None]
            if missing:
                print(f"  WARNING: could not find {', '.join(missing)} for {company} {year}")

            records.append({"Company": company, "Year": year, **financials})

    df = export_to_csv(records, "financial_data.csv")
    print("\nProcessing complete! Final dataset:")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()