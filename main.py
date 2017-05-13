import sys
import os
from quarry import *
from menu import *

running = True


def main():
    os.system('clear')
    while running is True:
        choose_menu()
        menu_chosing()


if __name__ == '__main__':
    main()
