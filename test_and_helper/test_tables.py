from database_access import *
cur, conn = database_access.get_database()

# Print all rows in table
cur.execute("SELECT * FROM people.data")
rows = cur.fetchall()
for row in rows:
    print(row, '\n')

cur.execute("SELECT * FROM people.names")
rows = cur.fetchall()
for row in rows:
    print(row, '\n')

cur.execute("SELECT * FROM nutrients.data")
rows = cur.fetchall()
for row in rows:
    print(row, '\n')
