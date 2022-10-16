import math
import pandas as pd
from datetime import date

data = pd.read_csv('nutrients_csvfile.csv')

# if user is already in database:
user_weight = input('Please enter your weight (lbs): ')
user_height = input('Please enter your height (inches): ')
user_sex = input('Please enter your sex(M or F): ')
user_age = input('Please enter your age: ')
curr_date = date.today()

foods = {}
print('Please enter the items you have eaten today. Please type done when you are finished.')
food = input()
while food.lower() != 'done':
    foods.append(food)
    food = input()

