import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def create():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()
    cur.execute("create table if not exists credentials (id serial primary key, username text, email text, password text)")
    conn.commit()
    conn.close()

def insert_new_details(username, email, password):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()
    cur.execute("insert into credentials (id, username, email, password) values(DEFAULT, %s, %s, %s)", (username, email, password))
    conn.commit()
    conn.close()

def verify(username, password):
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    cur = conn.cursor()
    cur.execute("select id from credentials where username=%s and password=%s", (username, password,))
    rows = cur.fetchall()
    conn.close()
    for r in rows:
        return r



