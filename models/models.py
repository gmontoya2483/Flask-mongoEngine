from db import db
from flask_mongoengine import MongoEngine


class Users(db.Document):
    name = db.StringField(max_length=60, unique=True)
    password = db.StringField(max_length=60)

