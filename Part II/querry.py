import psycopg2
from tabulate import tabulate

"""SQL handling module"""

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
