from flask import Flask
#from flask.extension.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from config import Config
from flask_migrate import Migrate
#from . routes import *
#from . models import User
#from forms import RegistrationForm
#from db import db,application
application = Flask(__name__)
#application = Flask(__name__, static_folder='../static')
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate= Migrate(application,db)
login = LoginManager(application)
login.login_view = 'login'

from application import routes, models
