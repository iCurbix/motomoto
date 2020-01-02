from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_cors import CORS
from src.config import Config
from src.auth.resources.auth import Register, Login, ValidateToken, Delete, RevokeToken
from src.db import db

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
migrate = Migrate(app, db)
CORS(app)

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(ValidateToken, '/validate')
api.add_resource(Delete, '/delete')
api.add_resource(RevokeToken, '/revoke')

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
#     app.run(port=5001, debug=True)
