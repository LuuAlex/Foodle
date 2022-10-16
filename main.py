# import stuff
from tabulate import tabulate
from test_and_helper.add_get_database import *
import add_user_entry

username = input('Please type your name to start: ')

user = int(input('''Welcome back to Foodle! Please choose what you would like to view today.
                Type 1 to add an entry of your daily intakes
                Type 2 to view a table of your daily intakes
                Type 3 to view a graph of the trends of your daily intakes
                 '''))


while user in [1, 2, 3]:
    if user == 1:
        add_user_entry.run(username)
        user = -1
"""
    elif user == 2:
        fi
    
    elif user == 3:

    else:
"""
        