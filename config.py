import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret-key'
FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
