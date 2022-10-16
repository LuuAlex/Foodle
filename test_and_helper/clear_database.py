# WARNING: DO NOT RUN THIS FILE. IT WILL DELETE EVERYTHING

from database_access import *
cur, conn = get_database()

cur.execute("DROP TABLE people.data")
cur.execute("DROP TABLE people.names")
cur.execute("DROP TABLE nutrients.data")

conn.commit()
cur.close()
