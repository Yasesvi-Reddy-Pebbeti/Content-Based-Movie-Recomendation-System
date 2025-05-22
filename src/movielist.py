import pandas as pd
import psycopg2
from dotenv import load_dotenv
import os

# Load DB credentials from .env
load_dotenv()

# Dynamically build the correct path to the CSV file
csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "movie_dataset.csv")

# Read the movie dataset
df = pd.read_csv(csv_path)
df = df.fillna('')  # Replace missing values with empty strings

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cur = conn.cursor()

inserted = 0
for index, row in df.iterrows():
    try:
        cur.execute("""
            INSERT INTO movielist (title, castt, director, genres)
            VALUES (%s, %s, %s, %s)
        """, (row['title'], row['cast'], row['director'], row['genres']))
        inserted += 1
    except Exception as e:
        print(f"❌ Skipping row {index}: {e}")

conn.commit()
conn.close()
print(f"✅ Inserted {inserted} movies into 'movielist' table.")
