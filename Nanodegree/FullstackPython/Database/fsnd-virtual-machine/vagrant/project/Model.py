import psycopg2


def open_connection():
    conn = psycopg2.connect("dbname=news user=vagrant password=vagrant")
    return conn


def close_connection(conn):
    conn.close()