# Import appropriate libraries,
import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
# This module defines that database parameters.
from config import Config
# Load the models (i.e. Courses, Registered Students model classes)
 from models import *
# Define an instance of flask application, load database parameters.
app = Flask (__name__)
app.config.from_object(Config)

# SQLAlchemy class need an instance of the flask app to know of the application model.
db.init_app(app)

def main():
    db.create_all()

# Define a route
@app.route('/')
def welcome():
    courses= db.execute("SELECT * from Course")
    return render_template('index.html', courses=courses)

# Define a route
@app.route('/add_course', methods = ["POST"])
def add_course():
    if request.method == 'POST':
        course_title = request.form.get("course_number")
        course_number = request.form.get("course_title")
        registered_students = courses.registered_students
        db.session.add(courses)
    return render_template("index.html", courses=courses, registered_students=registered_students)

# Define a route
@app.route('/register_student', methods = ["GET","POST"])
def register_students():
    courses= Course.query.get(course_id)
    registered_students= RegisteredStudent.query.get(id)
        if request.method == 'POST':
            name = request.form.get("name")
            grade = request.form.get("grade")
            db.session.add(register_students)
    return render_template("course_details.html", courses=courses, registered_students)
