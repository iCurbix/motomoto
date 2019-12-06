import datetime
from src.db import db
from src.models.alert import AlertModel


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    email = db.Column(db.String(100))
    alerts = db.relationship('AlertModel')
    registerdate = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.registerdate = datetime.datetime.utcnow()

    @classmethod
    def get_by_username(cls, username):
        user = cls.query.filter_by(username=username).first()
        if user:
            return user
        return None

    @classmethod
    def get_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        if user:
            return user
        return None

    @classmethod
    def get_by_id(cls, _id):
        user = cls.query.filter_by(id=_id).first()
        if user:
            return user
        return None

    def add_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        for alert in self.alerts:
            alert.delete_alert()
        db.session.delete(self)
        db.session.commit()
