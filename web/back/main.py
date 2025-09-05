from flask import Flask, request
from flask import jsonify
import psycopg2
import re
import datetime
from psycopg2.extras import RealDictCursor

# https://planetscale.com/blog/mysql-pagination
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

connection = psycopg2.connect(database="dob_web", user="dob_user", password="dob_pass", host="localhost", port=5432)

cursor = connection.cursor(cursor_factory=RealDictCursor)

cursor.execute("SELECT * FROM famous;")

endpoints = ["/api/v0/endpoints", "/api/v0/famous", "/api/v0/famous/{id}", "/api/v0/famous/today", "/api/v0/famous/date/<string:date>"]

@app.route("/api/v0/endpoints")
@app.route("/api/v0/")
def show_routes():
    return jsonify(endpoints)

@app.route("/api/v0/famous")
def famous_getAll():
    page = request.args.get('page')
    if page is None:
        page = 1;
    query = "SELECT * FROM famous ORDER BY id LIMIT 10 offset " + str(((int(page) - 1) * 10))
    print(query)
    cursor.execute(query)
    famous = cursor.fetchall()
    return jsonify(famous)

@app.route("/api/v0/famous/<int:id>")
def famous_detail(id):
    query = "SELECT * FROM famous WHERE id=" + str(id)
    cursor.execute(query)
    famous = cursor.fetchall()
    print(famous)
    return jsonify(famous)

@app.route("/api/v0/famous/date/<string:date>")
def famous_date(date):
    pattern = "^\d{4}-\d{2}-\d{2}$"
    if not re.match(pattern, date):
        return jsonify("Invalid date format"), 400
    query = "SELECT * FROM famous where birth_date='" + str(date) + "'"
    cursor.execute(query)
    famous = cursor.fetchall()
    return jsonify(famous)
    
@app.route("/api/v0/famous/today")
def famous_today():
    print(datetime.date.today())
    query = "SELECT * FROM famous WHERE birth_date='" + str(datetime.date.today()) + "'"
    print(query)
    cursor.execute(query)
    famous = cursor.fetchall()
    print(famous)
    return jsonify(famous)

