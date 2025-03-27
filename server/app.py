#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response, jsonify
from flask_restful import Resource
from flask_migrate import Migrate

# Local imports
from config import app, db, api
# Add your model imports
from models import User, Goal, Workout, Exercise



# Views go here!

@app.route('/')
def home():
    return '<h1>Recent Workouts and Progress Summary</h1>'

@app.route('/users')
def user_info():
    all_users = User.query.all()
    user_dictionary = [user.to_dict(only=('id', 'username', 'email', 'height', 'weight', 'fitness_level')) for user in all_users]
    return make_response(jsonify(user_dictionary), 200)

@app.route('/users/<int:id>')
def user_by_id(id):
    user = db.session.get(User, id)
    if user:
        response_body = user.to_dict()
        response_body ["number_of_goals"] = len(user.goals)
        return make_response(response_body, 200)
    else:
        response_body = {
            "error": "User not found"
        }
        return make_response(response_body, 404)

@app.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')
    height = request.json.get('height')
    weight = request.json.get('weight')
    fitness_level = request.json.get('fitness_level')
    try:
        new_user = User(username=username, email=email, password_hash=password, height=height, weight=weight, fitness_level=fitness_level)
        db.session.add(new_user)
        db.session.commit()
        response_body = new_user.to_dict(rules=('-workouts', '-goals',))
        return make_response(jsonify(response_body), 201)
    except ValueError:
        response_body = {
            "errors": ["validation errors"]
        }
        return make_response(jsonify(response_body), 422)

@app.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    user = db.session.get(User, id)

    if not user:
        response_body = {
            "error": "User not found"
        }
        return make_response(jsonify(response_body), 404)
    else:
        try:
            for attr in request.json:
                setattr(user, attr, request.json.get(attr))
            db.session.commit()
            response_body = user.to_dict(rules=('-goals',))
            return make_response(jsonify(response_body), 202)
        except ValueError:
            response_body = {
                "errors": ["validation errors"]
            }
            return make_response(jsonify(response_body), 400)

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = db.session.get(User, id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return make_response({}, 204)
    else:
        response_body = {
            "error": "User not found"
        }
        return make_response(jsonify(response_body), 404)



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

