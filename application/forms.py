from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, DateTimeField
from flask_table import Table, Col
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application.models import Users
from flask_login import current_user

class AddUserForm(FlaskForm):
    firstName = StringField()
    lastName = StringField()
    activityDate = DateTimeField()
    activityDesc = StringField()
    objRating = StringField()
    joyRating = StringField()
    
class AddForm(FlaskForm):
    activityDate = DateTimeField('Date', format='%d-%m-%Y',
       validators = [DataRequired('please select activity date')
       ]
    )
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

class LoginForm(FlaskForm):
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField('Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class DisplayForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

# Declare your table for activities display
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

# Get some objects for table
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description

items = [Item('Name1', 'Description1'),
         Item('Name2', 'Description2'),
         Item('Name3', 'Description3')]

class ModifyForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')


    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')
    