from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    tdate = db.Column(db.String(128), index=True, unique=False)
    weight_of_ort = db.Column(db.String(128), index=True, unique=False)
    weight_of_compost = db.Column(db.String(128), index=True, unique=False)
    groups = db.Column(db.String(128), index=True, unique=False)

#add columns here
    def __init__(self, notes, uname, product_name, product_description, help):
        self.notes = notes
        self.date = date
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
