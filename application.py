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

@application.route('/', methods=['GET', 'POST'])
@application.route('/index', methods=['GET', 'POST'])
def index():
    return "hello world"

@application.route('/bview', methods=['GET', 'POST'])
def bview():
    #form2 = RetrieveDBInfo(request.form)
#not chained
    #if request.method == 'POST' and form2.validate():
    try:
        #num_return = int(form2.numRetrieve.data)
        query_db = Data.query.order_by(Data.id.desc())#took out .limit(num_return)
        for q in query_db:
            print(q.notes)
        db.session.close()
    except:
        db.session.rollback()
    return render_template('results.html', results=query_db)

    #return render_template('bview.html', form1=form2)




@application.route('/bform', methods=['GET', 'POST'])
#@login_required
def bform():
    form1 = EnterDBInfo(request.form)

    if request.method == 'POST' and form1.validate():
        data_entered = Data(notes = form1.dbNotes.data, wdate = form1.dbDate.data, weight_of_ort = form1.dbWeight_of_ORT.data, weight_of_compost = form1.dbWeight_of_Compost.data, groups = form1.dbGroups.data)
        try:
            db.session.add(data_entered)
            db.session.commit()
            db.session.close()
        except:
            db.session.rollback()
        return render_template('thanks.html', notes=form1.dbNotes.data)
    return render_template('bform.html', form1=form1)

if __name__ == '__main__':
    application.run(host='0.0.0.0')
