import psycopg2
import logging
import dotenv
from contextlib import contextmanager

config = dotenv.dotenv_values(".env")


@contextmanager
def create_connect():
    try:
        conn = psycopg2.connect(f"dbname={config['POSTGRES_BASE']} user={config['POSTGRES_USER']} host={config['POSTGRES_HOST']} password={config['POSTGRES_PASS']}")
        try:
            yield conn
            conn.commit()
        finally:
            conn.close()
    except psycopg2.OperationalError:
        print("Connection failed")


def execute_query(conn, query, *args):
    cur = conn.cursor()
    try:
        cur.execute(query, args)
        conn.commit()
    except psycopg2.DatabaseError as err:
        logging.error(f"Database error: {err}")
        conn.rollback()
    finally:
        cur.close()