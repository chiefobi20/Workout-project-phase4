#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request
from flask_restful import Resource
from flask_migrate import Migrate

# Local imports
from config import app, db, api
# Add your model imports
from models import db, User, Goal, Workout, Exercise

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE


# Views go here!

@app.route('/')
def home():
    return '<h1>Recent Workouts and Progress Summary</h1>'

@app.route('/profile')
def user_info():
    return '<h1>Biometrics and Stats</h1>'

@app.route('/workouts')
def get_workouts():
    return '<h1>Workout Creation and History</h1>'

@app.route('/exercises')
def get_exercise():
    return '<h1>Exercise Library</h1>'


@app.route('/workouts/<int:id>')
def get_workout():
    pass

@app.route('/goals')
def manage_goals():
    pass




if __name__ == '__main__':
    app.run(port=5555, debug=True)

