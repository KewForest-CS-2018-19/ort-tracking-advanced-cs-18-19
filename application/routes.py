"""
from flask_login import current_user, login_user
from .models import User
from flask_login import logout_user
from . import db
from .forms import RegistrationForm
"""
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from application import application, db
from application.forms import RegistrationForm, LoginForm, EnterDBInfo, RetrieveDBInfo
from application.models import User, Data, School
# ...
@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def home():
    return render_template('rankings.html')

@application.route('/view', methods=['GET', 'POST'])
@login_required
def bview():
    #form2 = RetrieveDBInfo(request.form)
#not chained
    #if request.method == 'POST' and form2.validate():
    print(current_user.school_id)
    try:
        #num_return = int(form2.numRetrieve.data)
        query_db = Data.query.order_by(Data.id.desc())#took out .limit(num_return)
        #query_db = Data.query.filter(Data.school).order_by(Data.id.desc())#took out .limit(num_return)
        for q in query_db:
            print(q.notes)
        db.session.close()
    except:
        db.session.rollback()
    total_ort=0
    total_g=0
    for i in query_db:
        total_ort+= float(i.weight_of_ort)
        total_g += float(i.weight_of_compost)
    print(total_ort,total_g)

    return render_template('results.html', results=query_db, total_ort=total_ort, total_g=total_g)

    #return render_template('bview.html', form1=form2)

@application.route('/bform', methods=['GET', 'POST'])
@login_required
def bform():
    form1 = EnterDBInfo(request.form)

    if request.method == 'POST' and form1.validate():
        data_entered = Data(notes = form1.dbNotes.data, wdate = form1.dbDate.data, weight_of_ort = form1.dbWeight_of_ORT.data, weight_of_compost = form1.dbWeight_of_Compost.data, groups = form1.dbGroups.data)
        #data_entered = Data( weight_of_ort = form1.dbWeight_of_ORT.data, weight_of_compost = form1.dbWeight_of_Compost.data, groups = form1.dbGroups.data)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', notes=form1.dbNotes.data)
    return render_template('bform.html', form1=form1)


@application.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('bform'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('bform')
        return redirect(url_for('bform'))
    return render_template('login.html', title='Sign In', form=form)

@application.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('bview'))

@application.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit(): #submission has been validated on front end
        #print("school",form.schoolid.data)
        if form.schoolid.data == 0:
            school = School(name=form.school.data)
            print(school)
            db.session.add(school)
            db.session.commit()
            #print(school.name)
            newschool=School.query.filter(School.name == school.name).first()
            print(newschool.id)
            user = User(username=form.username.data, email=form.email.data, school_id=newschool.id)
        else:
            user = User(username=form.username.data, email=form.email.data, school_id=form.schoolid.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    #going to query the wschools table here
    slist=School.query.order_by(School.id.asc())
    #print(slist)
    return render_template('register.html', title='Register', form=form, slist=slist)


@application.route('/about')
def about():
    return render_template('about.html', title = 'About')

@application.route('/rankings')
def rankings():
    return render_template('rankings.html', title = 'My School')
