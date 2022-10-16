from test_and_helper.database_access import *
cur, conn = get_database()

def add_entry(user_id, date, sex, age, height, weight, caloric_intake, protein_grams_intake, carb_grams_intake, fat_grams_intake):
    cur.execute("""INSERT INTO people.data VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, date, sex, age, height, weight, caloric_intake, protein_grams_intake, carb_grams_intake, fat_grams_intake))
    rows = cur.fetchall()

def get_intake(food, column_int):
    cur.execute("SELECT * FROM nutrients.data WHERE food=%s", (food))
    return cur.fetchall(column_int)
    
