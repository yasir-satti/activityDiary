# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application.models import Activities, Users
from application.forms import AddUserForm, AddForm, DisplayForm, ModifyForm, DeleteForm
from application import app, db

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
    userdata = db.session.query(Users).all()
    activitydata = db.session.query(Activities).first()
    form = DisplayForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        return render_template('activitydisplay.html', form=form, title='Display Activity', userdata=userdata, activitydata=activitydata)
    
@app.route('/activitymd', methods=['GET', 'POST'])
def activitymd():
    form = ModifyForm()
    data = db.session.query(Activities).all()
    if form.validate_on_submit():
        data.activityDesc=form.activityDesc.data
        data.ObjRating=form.objRating.data
        data.JoyRating=form.joyRating.data  
        db.session.commit()        
        return redirect(url_for('home'))
    elif request.method == 'GET':
        user = data.user_id
        form.activityDesc.data=data.activityDesc
        form.objRating.data=data.ObjRating
        form.objRating.data=data.ObjRating
        form.joyRating.data=data.JoyRating
        return render_template('activitymd.html', title='Modify Activity - Select user', form=form, user=user, data=data)
    else:
        print(form.errors)    
    return render_template('activitymd.html', title='Modify Activity')

@app.route('/activitydelete', methods=['GET', 'POST'])
def activitydelete():
    form = DeleteForm()
    if form.validate_on_submit():
        data = Activities.query.first()
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        data = Activities.query.first()
        user = data.user_id
        form.activityDesc.data=data.activityDesc,
        form.objRating.data=data.ObjRating,
        form.joyRating.data=data.JoyRating
        return render_template('activitydelete.html', title='Delete Activity', form=form, user=user, data=data)
    else:
        print(form.errors)    
    return render_template('activitydelete.html', title='Delete Activity', form=form)

@app.route('/activitydelete/button', methods=["GET", "POST"])
def activitydeleteButton(): 
    activity = Activities.query.first()
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for('home'))
