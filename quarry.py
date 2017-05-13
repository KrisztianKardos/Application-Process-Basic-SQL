import psycopg2
from headers import *
from tabulate import tabulate

"""SQL database handling module"""

try:
    conn_string = "host='localhost' dbname='freka' user='freka' password='N4r4ncss4rg4'"
except:
    print("Unable to connect to the DB")

conn = psycopg2.connect(conn_string)
cursor = conn.cursor()


def print_table(table, headers):
    print(tabulate(table, headers, tablefmt="psql"))


def name_of_mentors():
    cursor.execute("SELECT first_name, last_name FROM mentors;")
    mentor_names = cursor.fetchall()
    print_table(mentor_names, headers=HEADERS["Menu1"])


def nick_of_mentors():
    cursor.execute("SELECT nick_name FROM mentors WHERE city = 'Miskolc';")
    mentor_nick_names = cursor.fetchall()
    print_table(mentor_nick_names, headers=HEADERS["Menu2"])


def carol_information():


def misterious_girl_hat():


def new_applicant():


def new_phonenumber():


def delete_applicants():