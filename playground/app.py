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

# Define a route
@app.route("/")



courses= Course.query.all()
return render_template('index.html', courses=courses)
