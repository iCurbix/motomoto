from flask import Flask
from flask_restful import Api
from src.alerts.config import Config
from src.alerts.resources.alerts import Alert, Alerts, ChangeActive

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

api.add_resource(Alert, '/alert')
api.add_resource(Alerts, '/alerts/<string:username>')
api.add_resource(ChangeActive, '/changeactive')

if __name__ == '__main__':
    from src.db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(port=5002, debug=True)
