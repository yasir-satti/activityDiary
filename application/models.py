from application import db
from flask_login import UserMixin
from datetime import datetime

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activityDesc = db.Column(db.String(500), nullable=False, unique=True)

    # print result of the operation, helps to see if something gone wrong
    def __repr__(self):
        return ''.join([
        'Activity ID: ', self.id, '\r\n',
        'Activity Desc: ', self.activityDesc])

#create columns in table
class Activities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activityDate = db.Column(db.Date, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey('activity.id'), nullable=False)
    ObjRating = db.Column(db.Integer, nullable=False)
    JoyRating = db.Column(db.Integer, nullable=False)
    activities = db.relationship('Activity', backref='ref', lazy=True)

    # print result of the operation, helps to see if something gone wrong
    def __repr__(self):
        return ''.join([
        'User ID: ', self.user_id, '\r\n',
        'Activity ID: ', self.id, '\r\n'])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ',
            'Last name: ', self.last_name])

        def __repr__(self):
            return ''.join(['UserID: ', str(self.id), '\r\n',
            'Email: ', self.email])

#@login_manager.user_loader
#def load_user(id):
#    return Users.query.get(int(id))