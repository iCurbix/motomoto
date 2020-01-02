from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from src.config import Config
from src.alerts.resources.alerts import Alert, Alerts, ChangeActive
from src.db import db

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
migrate = Migrate(app, db)

api.add_resource(Alert, '/alert')
api.add_resource(Alerts, '/alerts/<string:username>')
api.add_resource(ChangeActive, '/changeactive')

db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()

# if __name__ == '__main__':
#     from src.db import db
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()
#         db.session.commit()
#     app.run(port=5002, debug=True)
