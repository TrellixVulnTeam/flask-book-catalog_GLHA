import os
DEBUG = True
SECRET_KEY = 'topsecret'
#SQLALCHEMY_DATABASE_URI='postgresql://postgres:topsecret@localhost/catalog_db'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False


# DEBUG = False
# SECRET_KEY = 'topsecret'
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:123@localhost/catalog_db'
# SQLALCHEMY_TRACK_MODIFICATIONS = False