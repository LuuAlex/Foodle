"DO"
import os
import psycopg2

conn = psycopg2.connect("postgresql://foodle-admin:RGNOgu1FNDcqQffFb_px7Q@free-tier9.gcp-us-west2.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dfoodle-1453")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE data (
    user_id STRING,
    sex STRING,
    age INT,
    height DECIMAL,
    weight DECIMAL,
    caloric_intake DECIMAL,
    protein_grams_intake DECIMAL,
    carb_grams_intake DECIMAL,
    fat_grams_intake DECIMAL
    )
""")

cur.execute("""
    CREATE TABLE people (
    user_id STRING,
    name STRING
    )
""")



