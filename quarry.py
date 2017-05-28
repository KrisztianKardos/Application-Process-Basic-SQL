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
    cursor.execute("SELECT first_name|| ' ' ||last_name, phone_number FROM applicants\
                    WHERE first_name = 'Carol';")
    carol_name_phone = cursor.fetchall()
    print_table(carol_name_phone, headers=HEADERS["Menu3"])


def misterious_girl_hat():
    cursor.execute("SELECT first_name|| ' ' ||last_name, phone_number FROM applicants\
                    WHERE email LIKE '%@adipiscingenimmi.edu';")
    misterious_girl_name_phone = cursor.fetchall()
    print_table(misterious_girl_name_phone, headers=HEADERS["Menu4"]) 


def new_applicant():
    cursor.execute("INSERT INTO applicants\
                    (first_name, last_name, phone_number, email, application_code)\
                    VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');")
    cursor.execute("SELECT * FROM applicants WHERE application_code = '54823';")
    new_applicants = cursor.fetchall()
    print_table(new_applicants, headers=HEADERS["Menu5"])

 
def new_phonenumber():
    cursor.execute("UPDATE applicants SET phone_number = '003670/223-7459'\
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman';")
    cursor.execute("SELECT first_name|| ' ' ||last_name, phone_number FROM applicants\
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman';")
    update_applicant = cursor.fetchall()
    print_table(update_applicant, headers=HEADERS["Menu6"])


def delete_applicants():
    cursor.execute("DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';")
    delete_applicant = cursor.fetchall()
    print_table(delete_applicant, headers=HEADERS["Menu7"])