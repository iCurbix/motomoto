from flask import Flask
from flask_restful import Api
from src.mail.config import Config
from src.mail.resources.mail import RegisterMail, AlertMail

app = Flask(__name__, template_folder='../../templates')
app.config.from_object(Config)
api = Api(app)

api.add_resource(RegisterMail, '/registermail')
api.add_resource(AlertMail, '/alertmail')

if __name__ == '__main__':
    from src.db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(port=5005, debug=True)
