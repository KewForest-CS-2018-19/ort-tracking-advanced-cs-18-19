from application import db

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)
    uname = db.Column(db.String(128), index=True, unique=False)
    product_name = db.Column(db.String(128), index=True, unique=False)
    product_description = db.Column(db.String(128), index=True, unique=False)
    help = db.Column(db.String(128), index=True, unique=False)

#add columns here
    def __init__(self, notes, uname, product_name, product_description, help):
        self.notes = notes
        self.uname = uname
        self.product_name = product_name
        self.product_description = product_description
        self.help = help

    def __repr__(self):
        return '<Data %r>' % self.notes
