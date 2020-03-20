# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application.models import Activities, Users
from application import app, db

# define routes for / & /home, this function will be called when these are accessed

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
    
@app.route('/activityadd')
def activityadd():
    return render_template('activityadd.html', title='Add New Activity')

@app.route('/activitydisplay')
def activitydisplay():
    return render_template('activitydisplay.html', title='Display Activity')

@app.route('/activitymd')
def activitymd():
    return render_template('activitymd.html', title='Modify Activity')
    
@app.route('/activitydelete')
def activitydelete(): 
    return render_template('activitydelete.html', title='Delete Activity')
