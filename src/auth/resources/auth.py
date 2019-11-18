import jwt
import time
from flask import current_app
from flask_restful import Resource, request
from src.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash


class Register(Resource):
    def post(self):
        data = request.get_json()
        if None in [data.get('username'), data.get('username'), data.get('email')]:
            return {'message': 'data not correct'}, 400
        if User.get_by_username(data['username']) is None:
            User(data['username'], generate_password_hash(data['password']), data['email']).add_user()
            return {'message': 'user registered successfully'}, 201
        else:
            return {'message': 'user with this username already exists'}, 400


class Login(Resource):
    def post(self):
        data = request.get_json()
        if data.get('username') is None or data.get('username') is None:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(data['username'])
        if user and check_password_hash(user.password, data['password']):
            key = current_app.config['PRIVATE_KEY']
            now = int(time.time())
            token = {
                'iss': 'https://motomotoorsthlikethat.com',
                'aud': data['username'],
                'iat': now,
                'exp': now + 3600 * 24
            }
            token = jwt.encode(token, key, algorithm='RS512')
            return {
                'access-token': token.decode('utf8')
            }, 201
        else:
            return {'message': 'username or password incorrect'}, 401
