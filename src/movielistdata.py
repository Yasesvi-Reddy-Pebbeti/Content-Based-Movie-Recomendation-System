import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def search_movie_details(title=""):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()
    cur.execute("select title, castt, director, genres from movielist where title=%s", (title,))
    rows = cur.fetchall()
    conn.close()
    for r in rows:
        return rows
