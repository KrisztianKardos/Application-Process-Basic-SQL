"""SQL database handling module"""

conn_string = "host='localhost' dbname='freka' user='freka' password='N4r4ncss4rg4'"
try:
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
except:
    print("Unable to connect to the DB")