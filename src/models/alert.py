from src.db import db


class AlertModel(db.Model):
    __tablename__ = 'alerts'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    product = db.Column(db.String(255))
    price = db.Column(db.Float(precision=2))
    active = db.Column(db.Boolean, default=True)

    def __init__(self, user_id, product, price):
        self.user = user_id
        self.product = product
        self.price = price
        self.active = True

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user,
            'product': self.product,
            'price': self.price,
            'active': self.active,
        }

    def add_alert(self):
        db.session.add(self)
        db.session.commit()

    def delete_alert(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_alerts_by_user_id(cls, user):
        alerts = cls.query.filter_by(user=user).all()
        return alerts

    @classmethod
    def get_alert_by_id(cls, _id):
        alert = cls.query.filter_by(id=_id).first()
        if alert:
            return alert
        return None

    @classmethod
    def list_to_dict(cls, alertlist):
        return [alert.to_dict() for alert in alertlist]

    def update_info(self, product, price):
        self.product = product
        self.price = price
        db.session.commit()

    def change_active(self):
        self.active = not self.active
        db.session.commit()
