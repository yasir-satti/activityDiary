from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField, DateField
from flask_table import Table, Col
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application.models import Users
from flask_login import current_user
   
class AddForm(FlaskForm):
    activityDate = StringField('Date',
        validators = [
            DataRequired('please enter the activity description'),
            format('%d%m%y')
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
    activityDesc = StringField()
    objRating = StringField()
    joyRating = StringField()
    submit = SubmitField('Ok')

class ModifyForm(FlaskForm):
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
    submit = SubmitField('Delete')

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')

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