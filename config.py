import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/microblog'
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
DATABASE_URL = 'postgres://xtefhetoihpwql:YHz8u78DsGMTovDOkSuqgpEEc7@ec2-54-163-238-73.compute-1.amazonaws.com:5432/d4e3mgcabgh25n'
SQLALCHEMY_TRACK_MODIFICATIONS = False

FLASKY_ADMIN = 'johnngugi'
