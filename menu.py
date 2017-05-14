import sys
import os
from quarry import *


def choose_menu():
    print("Please select an option:")
    menu_options = [
                    "Name of mentors",
                    "Nick names of mentors",
                    "Carol's information",
                    "Misterious girl's hat",
                    "New applicant",
                    "New phonenumber",
                    "Delete applicants"
                    ]
    for index, option in enumerate(menu_options):
        print("{0} {1}".format(index + 1, option))
    print("0 {0}".format("Exit"))


def menu_chosing():
    select = int()
    while not select:
        select = input()
        if select == "":
            choose_menu()
        elif select == "0":
            running = False
            sys.exit()
        elif select == "1":
            os.system("clear")
            name_of_mentors()
        elif select == "2":
            os.system("clear")
            nick_of_mentors()
        elif select == "3":
            os.system("clear")
            carol_information()
        elif select == "4":
            os.system("clear")
            misterious_girl_hat()
        elif select == "5":
            os.system("clear")
            new_applicant()
        elif select == "6":
            os.system("clear")
            new_phonenumber()
        elif select == "7":
            os.system("clear")
            delete_applicants()
