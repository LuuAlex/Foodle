# import stuff
from tabulate import tabulate
from test_and_helper.add_get_database import *
from add_user_entry import *

username = input('Please type your name to start.')

user = input('''Welcome back to Foodle! Please choose what you would like to view today.
                Type 1 to add an entry of your daily intakes
                Type 2 to view a table of your daily intakes
                Type 3 to view a graph of the trends of your daily intakes
                 ''')


while user in [1, 2, 3]:
    if user == 2:
        data = get_user_data(username)
        
        print(data)
        print(tabulate(data, headers=['Caloric Intake', 'Protein Intake', 'Fat Intake', 'Carbohydrate Intake']))

        