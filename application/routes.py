# import render_template function from the flask module
from flask import render_template, redirect, url_for, request
from application.models import Activities, Users
from application.forms import AddUserForm, AddForm, DisplayForm, ModifyForm, DeleteForm
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
    # data = db.session.query(Users).join(Activities).filter(Activities.user_id == Users.id).all()
    userdata = db.session.query(Users).all()
    activitydata = db.session.query(Activities).all()
    form = DisplayForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        return render_template('activitydisplay.html', form=form, title='Display Activity', userdata=userdata, activitydata=activitydata)
    
@app.route('/activitymd')
def activitymd():
    form = ModifyForm()
    if form.validate_on_submit():
        modifyData = Activities (
            # activityDate=form.activityDate.data,
            activityDesc=form.activityDesc.data,
            ObjRating=form.objRating.data,
            JoyRating=form.joyRating.data
        )  
        # db.session.add(modifyData)
        db.session.commit()        
        return redirect(url_for('home'))
    elif request.method == 'GET':
        data = db.session.query(Activities).first()
        #userData = db.session.query(Users).filter_by(data.user_id)
        # user = userData.first_name + " " + userData.last_name
        user = data.user_id
        # form.activityUser.data=data.user_id,
        # form.activityDate.data=data.activityDate,
        form.activityDesc.data=data.activityDesc,
        form.objRating.data=data.ObjRating,
        form.joyRating.data=data.JoyRating
        return render_template('activitymd.html', title='Modify Activity - Select user', form=form, user=user, data=data)
    else:
        print(form.errors)    
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
    # data = db.session.query(Users).join(Activities).filter(Activities.user_id == Users.id).all()
    userdata = db.session.query(Users).all()
    activitydata = db.session.query(Activities).all()
    form = DeleteForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        return render_template('activitydelete.html', form=form, title='Delete Activity', userdata=userdata, activitydata=activitydata)
