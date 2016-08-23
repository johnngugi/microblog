import os
WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/microblog'
# SQLALCHEMY_DATABASE_URI = 'postgres://vfdmynrxdbkibv:q86zmPG0sAsWpTHiZMqGpL1rqn@ec2-54-225-100-236.compute-1.amazonaws.com:5432/dfs80bqrqhdp0g'
SQLALCHEMY_TRACK_MODIFICATIONS = False

FLASKY_ADMIN = 'johnngugi'
