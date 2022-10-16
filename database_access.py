import psycopg2

# Note: Regenerate Password In "test_password.txt" Before Use
password = open("test files/test_password.txt", "r").read()
# password = open("hidden files/real_password.txt", "r").read()

def get_database():
    conn = psycopg2.connect(f"postgresql://foodle-admin:{password}@free-tier9.gcp-us-west2.cockroachlabs.cloud:26257/defaultdb?sslmode=verify-full&options=--cluster%3Dfoodle-1453")
    cur = conn.cursor()
    return cur, conn