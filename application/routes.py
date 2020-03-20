# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application.models import Activities, Users
from application.forms import AddForm, DisplayForm, ModifyForm
from application import app, db

# define routes for / & /home, this function will be called when these are accessed

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
    
@app.route('/activityadd', methods=['GET', 'POST'])
def activityadd():
    form = AddForm()
    if form.validate_on_submit():
        addData = Activities (
            activityDate=form.activitydate.data,
            activityUser=form.user_id.data,
            activityDesc=form.activityDesc.data,
            objRating=form.objRating.data,
            joyRating=form.joyRating.data
        )  
        db.session.add(addData)
        db.session.commit()        
        return redirect(url_for('home'))    
    else:
        print(form.errors)    
    return render_template('activityadd.html', title='Add New Activity', form=form)

@app.route('/activitydisplay', methods=['GET', 'POST'])
def activitydisplay():
    form = DisplayForm()
    if request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name        
        form.email.data = current_user.email        
    return render_template('activitydisplay.html', title='Display Activity', form=form)

@app.route('/activitymd')
def activitymd():
    form = ModifyForm()
    if form.validate_on_submit():
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name        
        form.email.data = current_user.email        
    return render_template('activitydisplay.html', title='Modify Activity', form=form)
    
@app.route('/activitydelete')
def activitydelete(): 
    return render_template('activitydelete.html', title='Delete Activity')
