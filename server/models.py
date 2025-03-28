from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData


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


# Add relationship
    goals = db.relationship('Goal', back_populates='user', cascade="all")
    workouts = db.relationship('Workout', back_populates='user', cascade="all")

# Add serialization rules
    serialize_rules = ('-workouts.user', '-goals.user')

# Add validation
    @validates('username')
    def validates_username(self, key, value):
        if (value == None) or (not isinstance(value, str)) or (not (8 <= len(value) <= 20)):
            raise ValueError("Enter a username! Username must be between 8 and 20 characters")
        return value

    @validates('password')
    def validates_password(self, key, value):
        if (value == None) or (not isinstance(value, str)) or (len(value) < 9):
            raise ValueError("Enter a password! Password must be more than 8 characters")
        else:
            return value

    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.password_hash}, {self.email}, {self.height}, {self.weight}, {self.fitness_level}>'


class Goal(db.Model, SerializerMixin):
    __tablename__ = "goals"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)
    target_date = db.Column(db.String, nullable=False)
    completed = db.Column(db.String, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

# Add Goal relationship

    user = db.relationship('User', back_populates='goals')

# Add serialization rules

    def __repr__(self):
        return f'<Goal {self.id}: {self.description}, {self.target_date}, {self.completed}>'

class Workout(db.Model, SerializerMixin):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    duration = db.Column(db.String, nullable=True)
    date = db.Column(db.String, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    exercise_id = db.Column(db.Integer, db.ForeignKey("exercises.id"))

# Workout relationship goes here
    user = db.relationship("User", back_populates="workouts")
    exercise = db.relationship("Exercise", back_populates="workouts")

# Add serialization rules
    serialize_rules = ('-user.workouts', '-exercise.workouts')

    def __repr__(self):
        return f'<Workout {self.id}: {self.name}, {self.duration}, {self.date}>'


class Exercise(db.Model, SerializerMixin):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    body_part = db.Column(db.String, nullable=True)
    category = db.Column(db.String, nullable=True)
    demo_pic_url = db.Column(db.String, nullable=True)

# Exercise relationship goes here
    workouts = db.relationship("Workout", back_populates="exercise", cascade="all")

# Add serialization rules
    serialize_rules = ('-workouts.exercise',)

    def __repr__(self):
        return f'<Exercise {self.id}: {self.name}, {self.description}, {self.body_part}, {self.category}, {self.demo_pic_url}>'


