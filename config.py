
# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskdemo:flaskdemo@flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://davidaronson13:Hail00Rach03@flask-app-da.crmxs7h85wyq.us-east-2.rds.amazonaws.com:3306/flask-app-da'

# Uncomment the line below if you want to work with a local DB


import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///test2.db'


SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'

"""
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test2.db'
    SQLALCHEMY_POOL_RECYCLE = 3600
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
"""
