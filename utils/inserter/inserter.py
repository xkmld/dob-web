import psycopg2
import json

# initial data
input_folder_name = "data/"
scraped_data = "scraped/"
total_folder_name = input_folder_name + scraped_data;

connection = psycopg2.connect(database="dob_web", user="dob_user", password="dob_pass", host="localhost", port=5432)

cursor = connection.cursor()

cursor.execute("SELECT * FROM famous;")

# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database:- ", record)

cursor.close()
connection.close()
