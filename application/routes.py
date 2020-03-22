# import render_template function from the flask module
from flask import render_template, redirect, url_for, request

# import the app object from the ./application/__init__.py
from application.models import Activities, Users
from application.forms import RegistrationForm, AddForm, DisplayForm, ModifyForm, DeleteForm, LoginForm
from application import app, db, bcrypt

# import the relevant methods from flask login and your forms
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data)
        user = Users(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=hash_pw
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('activityadd'))
    return render_template('register.html', title='Register', form=form)

@app.route('/activityadd', methods=['GET', 'POST'])
@login_required
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
@login_required
def activitydisplay():
    userdata = db.session.query(Users).all()
    activitydata = db.session.query(Activities).all()
    form = DisplayForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        return render_template('activitydisplay.html', form=form, title='Display Activity', userdata=userdata, activitydata=activitydata)
    
@app.route('/activitymd', methods=['GET', 'POST'])
@login_required
def activitymd():
    form = ModifyForm()
    data = db.session.query(Activities).first()
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
@login_required
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
@login_required
def activitydeleteButton(): 
    activity = Activities.query.first()
    db.session.delete(activity)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
