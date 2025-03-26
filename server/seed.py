#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        User.query.delete()
        user1 = User(username="powerlifter20", password_hash ="a", email ="powerlifter123@email.com", height ="5'10\"", weight = 190.0, fitness_level ="Beginner", goals = 1)
        user2 = User(username = "gymrat42", password = "b", email = "gymrat123@email.com", height = "6'1\"", weight = 225.0, fitness_level = "Intermediate", goals = 1)
        user3 = User(username = "cardioislife", password = "p", email = "cardiorules45@email.com", height = "5'8\"", weight = 230, fitness_level = "Advanced", goals = 2)
        users = [user1, user2, user3]
        db.session.add_all(users)
        db.session.commit()
        print("Seeding successful!")
