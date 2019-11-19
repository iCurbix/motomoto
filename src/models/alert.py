from src.db import db


class AlertModel(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), db.ForeignKey('users.id'))
    product = db.Column(db.String(255))
    price = db.Column(db.Float(precision=2))
    active = db.Column(db.Boolean, default=True)

    def __init__(self, user, product, price):
        self.user = user
        self.product = product
        self.price = price
        self.active = True

    def add_alert(self):
        db.session.add(self)
        db.session.commit()

    def delete_alert(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_alerts_by_user_id(cls, user):
        alerts = cls.query.filter_by(user=user).all()
        return alerts
