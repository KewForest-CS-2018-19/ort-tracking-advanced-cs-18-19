from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    name = db.Column(db.String(128), index=True, unique=False)
    product name = db.Column(db.String(128), index=True, unique=False)
    product description = db.Column(db.String(128), index=True, unique=False)
    help = db.Column(db.String(128), index=True, unique=False)
#add columns here
    def __init__(self, notes):
        self.notes = notes

    def __repr__(self):
        return '<Data %r>' % self.notes
