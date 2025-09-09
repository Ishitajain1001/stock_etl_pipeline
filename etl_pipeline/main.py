# import psycopg2

# DB_HOST = "localhost"
# DB_NAME = "finance_data"
# DB_USER = "ishitajain"
# DB_PASS = "postgres123!"
# DB_PORT = 5433

# try:
#     conn = psycopg2.connect(
#         host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT
#     )
#     print("Connected to db")
#     conn.close()
# except Exception as e:
#     print("Connection failed")
#     print(e)

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()


def test_db_connection():
    db_url = os.getenv("DB_URL")
    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            print("Connected to db")
    except Exception as e:
        print("Connection failed")
        print(e)


if __name__ == "__main__":
    test_db_connection()
