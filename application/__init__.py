# import Flask class from the flask module
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# create a new instance of Flask and store it in app 
app = Flask(__name__)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from os import getenv
app.config['SECRET_KEY'] = getenv('SECRET_KEY')

# configer db connection
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:root@35.242.185.100/activityDiary'
# app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://yasir:qaacademy@localhost:3306/activityDiary'

# create db object
db = SQLAlchemy(app)

# import the ./application/routes.py file
from application import routes