from . import db
from werkzeug.security import generate_password_hash, check_password_hash
#from . import login


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    wdate = db.Column(db.Date(), index=True, unique=False)
    weight_of_ort = db.Column(db.String(128), index=True, unique=False)
    weight_of_compost = db.Column(db.String(128), index=True, unique=False)
    groups = db.Column(db.String(128), index=True, unique=False)

#add columns here
    def __init__(self, notes, wdate, weight_of_ort, weight_of_compost, groups):
        self.notes = notes
        self.wdate = wdate
        self.weight_of_ort = weight_of_ort
        self.weight_of_compost = weight_of_compost
        self.groups = groups

    def __repr__(self):
        return '<Data %r>' % self.notes

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.Date(), index=True, unique=False)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
