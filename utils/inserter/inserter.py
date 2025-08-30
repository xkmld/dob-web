import psycopg2

connection = psycopg2.connect(database="dob_web", user="dob_user", password="dob_pass", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * FROM famous;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)
