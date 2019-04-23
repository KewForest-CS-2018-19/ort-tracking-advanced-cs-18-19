from datetime import datetime
from application import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from flask_login import login_manager

#@login_manager.user_loader

class School (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    name = db.Column(db.String(64), index=True, unique=True)
    date_joined = db.Column(db.Date(), default= date.today, index=True, unique=False)
    url = db.Column(db.String(128), index=True, unique=True)
    number_of_students = db.Column(db.String(128), index=True, unique=False)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=False)
    password_hash= db.Column(db.String(128))
    posts = db.relationship('Data', backref = 'author', lazy ='dynamic' )
    date_joined = db.Column(db.Date(), default= date.today, index=True, unique=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader

def load_user(id):
    return User.query.get(int(id))
def get_user(id):
  return User.query.get(int(id))

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    wdate = db.Column(db.Date(), default= date.today, index=True, unique=False)
    weight_of_ort = db.Column(db.String(128), index=True, unique=False)
    weight_of_compost = db.Column(db.String(128), index=True, unique=False)
    groups = db.Column(db.String(128), index=True, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'))


#add columns here
    def __init__(self, notes, wdate, weight_of_ort, weight_of_compost, groups):
        self.notes = notes
        self.wdate = wdate
        self.weight_of_ort = weight_of_ort
        self.weight_of_compost = weight_of_compost
        self.groups = groups

    def __repr__(self):
        return '<Data %r>' % self.notes
