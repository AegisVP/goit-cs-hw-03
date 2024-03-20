import psycopg2
import logging
from contextlib import contextmanager


@contextmanager
def create_connect():
    try:
        conn = psycopg2.connect("dbname='hw_03' user='postgres' host='localhost' password='goit'")
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