from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    height = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    fitness_level = db.Column(db.String, nullable=False)
    goals = db.Column(db.Integer, nullable=False)

    # User Relationships go here!

class Goal(db.Model, SerializerMixin):
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    target_date = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Goal Relationship goes here!
    # user = db.relationship("User", back_populates="signups")

class Workout(db.Model, SerializerMixin):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    duration = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))

    # Workout relationship goes here!
    user = db.relationship("User", back_populates="workouts")
    exercise = db.relationship("Exercise", back_populates="workouts")

class Exercise(db.Model, SerializerMixin):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    body_part = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=True)
    demo_pic_url = db.Column(db.String, nullable=True)

    # Exercise relationship goes here!
    workouts = db.relationship("Workout", back_populates="exercise", cascade="all")



