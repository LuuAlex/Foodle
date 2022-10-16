from datetime import date
from test_and_helper.database_access import *
from test_and_helper.add_get_database import *

def run(username=None):
    if username == None:
        username = input('Please enter your name: ')
    info = get_user_info(username)
    if info:
        curr_date = date.today()
        #curr_date = date.today() + date.timedelta(days=1)
        user_sex = info[0]
        user_age = info[1]
        user_height = info[2]
        user_weight = info[3]
    else:
        user_weight = input('Please enter your weight (lbs): ')
        user_height = input('Please enter your height (inches): ')
        user_sex = input('Please enter your sex (M or F): ')
        user_age = input('Please enter your age: ')
        curr_date = date.today()

    foods = {}
    print('Please enter the items you have eaten today and the quantity. Please type "done" when you are finished. Example: 3 Carrots')
    food = input()
    while food.lower() != 'done':
        food = food.split()
        foods[food[1]] = food[0]
        food = input()

    def return_total_cals(foods):
        total_cals = 0
        for i in foods.keys():
            total_cals += (int(foods[i]) * float(get_intake(i, 3)))
        return total_cals

    def return_total_protein(foods):
        total_protein = 0
        for i in foods.keys():
            total_protein += (int(foods[i]) * float(get_intake(i, 4)))
        return total_protein

    def return_total_fat(foods):
        total_fat = 0
        for i in foods.keys():
            total_fat += (int(foods[i]) * float(get_intake(i, 5)))
        return total_fat

    def return_total_carbs(foods):
        total_carbs = 0
        for i in foods.keys():
            total_carbs += (int(foods[i]) * float(get_intake(i, 8)))
        return total_carbs

    add_entry(username, curr_date, user_sex, user_age, user_height, user_weight, return_total_cals(foods), return_total_protein(foods), return_total_carbs(foods), return_total_fat(foods))
