from flask import Flask, request
from flask import jsonify
import psycopg2
import re
import datetime
from psycopg2.extras import RealDictCursor
from flask_cors import CORS, cross_origin

# https://planetscale.com/blog/mysql-pagination
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#CORS(api, resources={r"/api/*": {"origins": "http://localhost:5173"}})
@app.route("/")
def hello_world():
    return "<p>Hello, World!<br>This is the backend.</p>"

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
    query = "SELECT * FROM famous WHERE DATE_PART('day', birth_date) = date_part('day', CURRENT_DATE) AND DATE_PART('month', birth_date) = date_part('month', CURRENT_DATE)"
    print(query)
    cursor.execute(query)
    famous = cursor.fetchall()
    print(famous)
    return jsonify(famous)

@app.route("/api/v0/famous/random")
def famous_random():
    query = "SELECT * FROM famous ORDER BY RANDOM() LIMIT 1"
    print(query)
    cursor.execute(query)
    famous = cursor.fetchall()
    return jsonify(famous)
