import os

class Config(object):
    priv_key_path = os.environ['PRIVKEY']
    pub_key_path = os.environ['PUBKEY']
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    with open(priv_key_path) as f:
        PRIVATE_KEY = f.read()

    with open(pub_key_path) as f:
        PUBLIC_KEY = f.read()
