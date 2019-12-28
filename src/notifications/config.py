import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DBURI') or 'sqlite:///../data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
