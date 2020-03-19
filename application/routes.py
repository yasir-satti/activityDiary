# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application.models import Activities, Users
from application import app, db

# define routes for / & /home, this function will be called when these are accessed

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/activitynew')
def activitynew(): 
    return render_template('activitynew.html', title='Create New Activity')

@app.route('/activityshow')
def activityshow():
    return render_template('activityshow.html', title='Show Activity')

@app.route('/activityadd')
def activityadd():
    return render_template('activityadd.html', title='Add Activity')

@app.route('/activitymd')
def activitymd():
    return render_template('activitymd.html', title='Modify/Delete Activity')
    