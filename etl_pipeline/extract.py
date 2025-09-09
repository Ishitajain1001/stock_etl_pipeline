from dotenv import load_dotenv
import requests
import pandas as pd
import os
import json
import time


def extract_data(symbols):
    load_dotenv()
    alpha_key = os.getenv("ALPHA_API_KEY")
    if alpha_key is None:
        print("Error: API key not found in .env file.")

    # https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo
    base_url = "https://www.alphavantage.co/query"

    for symbol in symbols:
        params = {"function": "OVERVIEW", "symbol": symbol, "apikey": alpha_key}

        r = requests.get(base_url, params=params)
        data = r.json()

        with open(f"data/raw/{symbol}.json", "w") as f:
            json.dump(data, f, indent=2)

        print(f"Saved data for {symbol}")
        time.sleep(12)


extract_data(["IBM", "AAPL", "GOOGL", "MSFT"])
