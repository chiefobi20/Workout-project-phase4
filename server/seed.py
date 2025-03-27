#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Exercise, Goal, Workout

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Deleting data...")
        # Seed code goes here!
        User.query.delete()
        Workout.query.delete()
        Exercise.query.delete()
        Goal.query.delete()

        print("Creating user...")
        user1 = User(username="powerlifter20", password_hash ="a", email ="powerlifter123@email.com", height ="5'10\"", weight = 190.0, fitness_level ="Beginner")
        user2 = User(username = "gymrat42", password_hash = "b", email = "gymrat123@email.com", height = "6'1\"", weight = 225.0, fitness_level = "Intermediate")
        user3 = User(username = "cardioislife", password_hash = "p", email = "cardiorules45@email.com", height = "5'8\"", weight = 230, fitness_level = "Advanced")
        users = [user1, user2, user3]

        print("Creating workouts...")
        person1 = Workout(name = "Lat Pulldowns", duration = "3 x 10", date = "01-15-2025")
        person1 = Workout(name = "Bicep Curls", duration = "3 x 15", date = "01-15-2025")
        person2 = Workout(name = "")


        print("Creating exercise...")
        exer1 = Exercise(name = "Lat Pulldowns", description = "To perform a lat pulldown, sit at a lat pulldown machine and grip the bar slightly wider than shoulder-width with an overhand grip. Keep your chest up and engage your core as you pull the bar down toward your upper chest, squeezing your shoulder blades together. Slowly return the bar to the starting position with control. Avoid using momentum and focus on a smooth, controlled movement for maximum muscle engagement.", body_part = "Lattissimus dorsi(lats), upper back, and biceps", category = "Lift", demo_pic_url = "")
        exer2 = Exercise(name = "Stairmaster", description = "To perform this exercise, step onto the machine and start at a moderate pace, keeping your back straight and hands lightly on the rails for support. Step naturally and controlled, driving through your heels to engage your glutes and avoid relying too much on the handrails. Maintain a steady pace and breathing rhythm, adjusting speed or resistance to increase intensity", body_part = "Quads, hamstrings, glutes, and calves", category = "Cardio", demo_pic_url = "")
        exer3 = Exercise(name = "Bicep Curls", description = "To perform a bicep curl, stand with feet shoulder-width apart, holding a dumbbell or barbell with an underhand grip. Keep your elbows close to your sides and curl the weight toward your shoulders by contracting your biceps. Lower the weight back down slowly and with control to the starting position. Keep your core engaged and avoid swinging for proper form", body_part = "Biceps", category = "Lift", demo_pic_url = "")


        db.session.add_all(users)
        db.session.commit()
        print("Seeding successful!")
