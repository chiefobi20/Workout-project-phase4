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
        user1 = User(username="powerlifter20", password_hash="a", email="powerlifter123@email.com", height="5'10\"", weight= 190.0, fitness_level="Beginner", profile_pic="powerlifter.jpeg")
        db.session.add_all([user1])
        db.session.commit()
        print("Seeding successful!")
