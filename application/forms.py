from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, DateField
from flask_table import Table, Col
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application.models import Users
from flask_login import current_user

class AddUserForm(FlaskForm):
    firstName = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    lastName = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Add')
    
class AddForm(FlaskForm):
    # activityDate = DateField('Date', format='%d-%m-%Y',
    #   validators = [DataRequired('please select activity date')
    #   ]
    # )
    activityUser = IntegerField('User id',
        validators = [
            DataRequired('please enter your user id'),
            NumberRange(min=1, max=999)
        ]
    )
    activityDesc = StringField('Activity Description',
        validators = [
            DataRequired('please enter the activity description'),
            Length(min=5, max=500)
        ]
    )
    objRating = IntegerField('Objective rating',
        validators = [
            DataRequired('please enter activity objective rating (1 to 10)'),
            NumberRange(min=1, max=10)
        ]
    )
    joyRating = IntegerField('Joy rating',
        validators = [
            DataRequired('please enter activity joy rating (1 to 10)'),
            NumberRange(min=1, max=10)
        ]
    )
    submit = SubmitField('Add')

class DisplayForm(FlaskForm):
    firstName = StringField()
    lastName = StringField()
    # activityDate = DateField()
    activityDesc = StringField()
    objRating = StringField()
    joyRating = StringField()
    submit = SubmitField('Ok')

class ModifyForm(FlaskForm):
    #activityDate = DateField('Date', format='%d-%m-%Y',
    #   validators = [DataRequired('please select activity date')
    #   ]
    #)
    activityUser = IntegerField('User id',
        validators = [
            DataRequired('please enter your user id'),
            NumberRange(min=1, max=999)
        ]
    )
    activityDesc = StringField('Activity Description',
        validators = [
            DataRequired('please enter the activity description'),
            Length(min=5, max=500)
        ]
    )
    objRating = IntegerField('Objective rating',
        validators = [
            DataRequired('please enter activity objective rating (1 to 10)'),
            NumberRange(min=1, max=10)
        ]
    )
    joyRating = IntegerField('Joy rating',
        validators = [
            DataRequired('please enter activity joy rating (1 to 10)'),
            NumberRange(min=1, max=10)
        ]
    )
    submit = SubmitField('Update')
    
class DeleteForm(FlaskForm):
    firstName = StringField()
    lastName = StringField()
    #activityDate = DateField()
    activityDesc = StringField()
    objRating = StringField()
    joyRating = StringField()
    submit = SubmitField('Delete')