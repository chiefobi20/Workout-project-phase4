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
    profile_pic = db.Column(db.String, nullable=False)