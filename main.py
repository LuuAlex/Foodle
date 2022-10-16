# import stuff
from tabulate import tabulate
from test_and_helper.add_get_database import *
import add_user_entry
import matplotlib.pyplot as p

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
    
    elif user == 2:
        data = get_user_data(username)
        print(data)
        print(tabulate(data, headers=['Caloric Intake', 'Protein Intake', 'Fat Intake', 'Carbohydrate Intake']))
        user = -1

    elif user == 3:
        x_axis, y_axis = [], []
        x = int(input('''
                    Please type in the graph you want to see:
                    1 - Get daily progress of caloric intake
                    2 - Get daily progress of protein intake
                    3 - Get daily progress of carbohydrate intake
                    4 - Get daily progress of fat intake
                    '''))
        if x == 1:
            for row in get_user_data(username):
                x_axis += [row[0]]
                y_axis += [row[1]]
            p.plot(x_axis, y_axis)
            p.xlabel('Date')
            p.ylabel('Caloric Intake')
            p.show()
        elif x == 2:
            for row in get_user_data(username):
                x_axis += [row[0]]
                y_axis += [row[2]]
            p.plot(x_axis, y_axis)
            p.xlabel('Date')
            p.ylabel('Protein Intake')
            p.show()
        elif x == 3:
            for row in get_user_data(username):
                x_axis += [row[0]]
                y_axis += [row[3]]
            p.plot(x_axis, y_axis)
            p.xlabel('Date')
            p.ylabel('Carbohydrate Intake')
            p.show()
        elif x == 4:
            for row in get_user_data(username):
                x_axis += [row[0]]
                y_axis += [row[4]]
            p.plot(x_axis, y_axis)
            p.xlabel('Date')
            p.ylabel('Fat Intake')
            p.show()
        else:
            x = input('Please type in a valid option.')
        user = -1
        
    else:
        user = input('Please type in a valid option.')
        