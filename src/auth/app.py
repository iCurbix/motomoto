from flask import Flask
from flask_restful import Api
from src.auth.config import Config
from src.auth.resources.auth import Register, Login, ValidateToken, Delete

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(ValidateToken, '/validate')
api.add_resource(Delete, '/delete')

if __name__ == '__main__':
    from src.db import db
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(port=5001, debug=True)
