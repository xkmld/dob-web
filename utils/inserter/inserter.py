import psycopg2
import os
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

all_files = os.listdir(total_folder_name)
all_files.remove("images")

# to prevent problems...
def return_if_exist(word):
    try:
        return d[word]
    except KeyError:
        return None

def check_if_null(word):
    if (word == "null"):
        return None
    return word
 
def parse_birth_date(date):
    if (date == ""):
        return None
    date_formated = (date[2] + "-" + date[0] + "-" + date[1]).replace(',','')
    if (len(date[2]) == 2):
        return None
    return date_formated

def process_name(name):
    return name.replace(' ', '').lower() + ".jpg"

for file in all_files:
    with open (total_folder_name + file) as f:
        d = json.load(f)
        #if (d['img'] is None):
        name = check_if_null(return_if_exist('name'))
        job = check_if_null(return_if_exist('job'))
        img = check_if_null(process_name(name))
        birth_date = check_if_null(return_if_exist('birth_date'))
        birth_date = parse_birth_date(birth_date)
        if (birth_date == None):
            continue
        birth_place = check_if_null(return_if_exist('birth_place'))
        about = check_if_null(return_if_exist('about'))
        before_fame = check_if_null(return_if_exist('before_fame'))
        curiosities = check_if_null(return_if_exist('curiosities'))
        family_life = check_if_null(return_if_exist('family_life'))
        association = check_if_null(return_if_exist('association'))
        cursor.execute("INSERT INTO famous (name, job, img, birth_date, birth_place, about, before_fame, curiosities, family_life, association) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, job, img, birth_date,birth_place, about, before_fame, curiosities, family_life, association))
            
connection.commit();
cursor.close()
connection.close()
