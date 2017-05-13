import sys
import os


def choose_menu():
    os.system("clear")
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
    selection = input("Please enter a number: ")


def menu_chosing():
    if selection = "":
        menu_selection[]
    if selection = "1":
        os.system("clear")
        name_of_mentors()
    if selection = "2":
        os.system("clear")
        nick_of_mentors()
    if selection = "3":
        os.system("clear")
        carol_information()
    if selection = "4":
        os.system("clear")
        misterious_girl_hat()
    if selection = "5":
        os.system("clear")
        new_applicant()
    if selection = "6":
        os.system("clear")
        new_phonenumber()
    if selection = "7":
        os.system("clear")
        delete_applicants()
