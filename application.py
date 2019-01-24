from application import application, db
from application.models import User, Data


@application.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Data': Data}

if __name__ == '__main__':
    application.run(host='127.0.0.1') #for PC
    #application.run(host='0.0.0.0') #for mac
