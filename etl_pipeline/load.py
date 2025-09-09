from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


def load_data(df):
    db_url = os.getenv("DB_URL")
    engine = create_engine(db_url)

    # Explicit connection for SQLAlchemy 2.x
    with engine.begin() as conn:
        df.to_sql("stock_fundamentals", con=conn, if_exists="replace", index=False)
    print("✅ Data successfully loaded into stock_fundamentals")


if __name__ == "__main__":
    df = pd.read_csv("data/processed/overview.csv")
    load_data(df)
