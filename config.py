import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/swamprdb'

CSRF_ENABLED = True # This is to prevent CSRF attacks-so that all submissions acutally come from our form
SECRET_KEY = 'big-secret'
