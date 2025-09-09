from etl_pipeline.extract import extract_data
from etl_pipeline.transform import transform_data
from etl_pipeline.load import load_data


def main():
    symbols = ["IBM", "AAPL", "GOOGL", "MSFT"]
    extract_data(symbols)
    df = transform_data()
    load_data(df)


if __name__ == "__main__":
    main()
