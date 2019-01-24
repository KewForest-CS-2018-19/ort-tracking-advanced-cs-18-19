'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS
Author: Scott Rodkey - rodkeyscott@gmail.com
Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''


from flask import Flask, render_template, request
from application import db
from application.models import Data
from application.forms import EnterDBInfo, RetrieveDBInfo



# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True
# change this to your own value
application.secret_key = 'cdg1312001GDC'
#application.secret_key = 'cC1YCIWOj9GgWspgNEo2'




if __name__ == '__main__':
    application.run(host='127.0.0.1') #for PC
    #application.run(host='0.0.0.0') #for mac
