# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application.models import Activities, Users
from application.forms import AddUserForm, AddForm, DisplayForm, ModifyForm
from application import app, db

# define routes for / & /home, this function will be called when these are accessed

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    form = AddUserForm()
    if form.validate_on_submit():
        addData = Users (
            first_name=form.firstName.data,
            last_name=form.lastName.data,
            email=form.email.data,
            )  
        db.session.add(addData)
        db.session.commit()        
        return redirect(url_for('home'))    
    else:
        print(form.errors)    
    return render_template('adduser.html', title='Add New User', form=form)


@app.route('/activityadd', methods=['GET', 'POST'])
def activityadd():
    form = AddForm()
    if form.validate_on_submit():
        addData = Activities (
            activitydate=form.activityDate.data,
            user_id=form.activityUser.data,
            activityDesc=form.activityDesc.data,
            ObjRating=form.objRating.data,
            JoyRating=form.joyRating.data
        )  
        db.session.add(addData)
        db.session.commit()        
        return redirect(url_for('home'))    
    else:
        print(form.errors)    
    return render_template('activityadd.html', title='Add New Activity', form=form)

@app.route('/activitydisplay', methods=['GET', 'POST'])
def activitydisplay():
    userData = Users.query.filter_by(id=1).first()
    displayData = Activities.query.filter_by(user_id=1).first()
    form = DisplayForm()
    if request.method == 'GET':
        form.first_name.label = userData.first_name
        form.last_name.label = userData.last_name        
        form.activityDesc.label = displayData.activityDesc
        form.objRating.label = displayData.ObjRating
        form.joyRating.label = displayData.JoyRating     
    return render_template('activitydisplay.html', title='Display Activity', form=form)
    
@app.route('/activitymd')
def activitymd():
    #form = ModifyForm()
    #if form.validate_on_submit():
    #    current_user.first_name = form.first_name.data
    ##    current_user.last_name = form.last_name.data
    #    current_user.email = form.email.data
    #    db.session.commit()
    #    return redirect(url_for('home'))
    #elif request.method == 'GET':
    #    form.first_name.data = current_user.first_name
    #    form.last_name.data = current_user.last_name        
    #    form.email.data = current_user.email        
    #return render_template('activitydisplay.html', title='Modify Activity', form=form)
    return render_template('activitymd.html', title='Modify Activity')

@app.route('/activitydelete')
def activitydelete(): 
    return render_template('activitydelete.html', title='Delete Activity')
