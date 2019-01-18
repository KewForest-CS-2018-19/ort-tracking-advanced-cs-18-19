from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from .models import User
from .forms import RegistrationForm
from db import db,application

#application = Flask(__name__)
#application.config.from_object('config')
#db = SQLAlchemy(application)

login = LoginManager(application)
#login.login_view = 'login'
