import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASSWORD")
    db_port = os.getenv("DB_PORT")
    connection = psycopg2.connect(dbname = db_name, host = db_host, password = db_pass, port = db_port, user = db_user)
    return connection

if __name__ == "__main__":
    conn = get_connection()
    print(conn)
    conn.close()