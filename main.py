import tabulate
import sys
import os
from quarry import *


def print_table():
    print(tabulate(table, headers, tablefmt="psql")