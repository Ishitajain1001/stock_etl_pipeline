import os
import json
import pandas as pd


def load_raw_data(data_dir="data/raw"):
    df = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(data_dir, filename)
            with open(filepath, "r") as file:
                raw_data = json.load(file)
                row = transform_single_row(raw_data)
                df.append(row)
    return pd.concat(df)


def parse_float(val):
    try:
        return float(val)
    except (ValueError, TypeError):
        return None


# need to check Alpha Vantage documentation and see if it's realistic
def parse_perc(val):
    try:
        new_val = float(val)
        # return new_val if new_val <= 1 else new_val / 100.0
        return new_val
    except:
        return None


def parse_int(val):
    try:
        return int(val)
    except (ValueError, TypeError):
        return None


def parse_string(val):
    try:
        return str(val).strip()
    except (AttributeError, ValueError, TypeError):
        return None


def transform_single_row(raw_data):
    return pd.DataFrame(
        [
            {
                "symbol": raw_data.get("Symbol"),
                "company_name": parse_string(raw_data.get("Name")),
                "sector": (
                    parse_string(raw_data.get("Sector")).title()
                    if parse_string(raw_data.get("Sector"))
                    else None
                ),
                "market_cap": parse_int(raw_data.get("MarketCapitalization")),
                "pe_ratio": parse_float(raw_data.get("PERatio")),
                "dividend_yield": parse_perc(raw_data.get("DividendYield")),
                "description": parse_string(raw_data.get("Description")),
                "exchange": parse_string(raw_data.get("Exchange")),
                "currency": parse_string(raw_data.get("Currency")),
                "country": parse_string(raw_data.get("Country")),
                "industry": (
                    parse_string(raw_data.get("Industry")).title()
                    if parse_string(raw_data.get("Industry"))
                    else None
                ),
                "peg_ratio": parse_float(raw_data.get("PEGRatio")),
                "book_val": parse_float(raw_data.get("BookValue")),
                "dividend_per_share": parse_float(raw_data.get("DividendPerShare")),
                "eps": parse_float(raw_data.get("EPS")),
                "revenue_ttm": parse_int(raw_data.get("RevenueTTM")),
                "profit_margin": parse_perc(raw_data.get("ProfitMargin")),
                "return_on_assets_ttm": parse_perc(raw_data.get("ReturnOnAssetsTTM")),
                "return_on_equity": parse_perc(raw_data.get("ReturnOnEquityTTM")),
                "high_52_week": parse_float(raw_data.get("52WeekHigh")),
                "low_52_week": parse_float(raw_data.get("52WeekLow")),
                "mov_avg_50d": parse_float(raw_data.get("50DayMovingAverage")),
                "mov_avg_200d": parse_float(raw_data.get("200DayMovingAverage")),
            }
        ]
    )


def transform_data():
    df = load_raw_data()
    df.to_csv("data/processed/overview.csv", index=False)
    return df


transform_data()
