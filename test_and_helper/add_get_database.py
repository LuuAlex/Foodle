from database_access import *
cur, conn = get_database()

def add_entry(user_id, date, sex, age, height, weight, caloric_intake, protein_grams_intake, carb_grams_intake, fat_grams_intake):
    cur.execute("""INSERT INTO people.data VALUES 
        (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (user_id, date, sex, age, height, weight, caloric_intake, protein_grams_intake, carb_grams_intake, fat_grams_intake))
    conn.commit()

def get_intake(food, column_int):
    cur.execute(f"SELECT * FROM nutrients.data WHERE food='{food}'")
    return cur.fetchall()[0][column_int]
    
