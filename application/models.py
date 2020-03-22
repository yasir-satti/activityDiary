from application import db
from datetime import datetime

#create columns in table
class Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activityDate = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    activityDesc = db.Column(db.String(500), nullable=False, unique=True)
    ObjRating = db.Column(db.Integer, nullable=False)
    JoyRating = db.Column(db.Integer, nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)