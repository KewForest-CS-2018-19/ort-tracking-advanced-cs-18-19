from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    date = db.Column(db.String(128), index=True, unique=False)
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
