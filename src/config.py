import os

try:
    priv_key_path = os.environ['PRIVKEY']
    pub_key_path = os.environ['PUBKEY']
except KeyError:
    pass


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DBURI') or 'sqlite:///../data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    try:
        with open(priv_key_path) as f:
            PRIVATE_KEY = f.read()

        with open(pub_key_path) as f:
            PUBLIC_KEY = f.read()
    except NameError:
        pass

    try:
        MAIL_USERNAME = os.environ['MAIL_USERNAME']
        MAIL_PASSWORD = os.environ['MAIL_PASSWORD']
        MAIL_SERVER = os.environ['MAIL_SERVER']
        MAIL_PORT = os.environ['MAIL_PORT']
    except KeyError:
        pass
