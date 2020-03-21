# import Flask class from the flask module
from flask import Flask

# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# create a new instance of Flask and store it in app 
app = Flask(__name__)

from os import getenv
# app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SECRET_KEY'] = '3409ri3049ir0934ir093i4r'

# configer db connection
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.242.185.100/activityDiary'

# create db object
db = SQLAlchemy(app)

# import the ./application/routes.py file
from application import routes