import jwt
import datetime
import requests
from flask import current_app, request
from flask_restful import Resource
from src.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from src.utils.checkauth import authrequired
from src.redisdb import rd


class Register(Resource):
    def put(self):
        data = request.get_json()
        if None in [data.get('username'), data.get('username'), data.get('email')]:
            return {'message': 'data not correct'}, 400
        if User.get_by_username(data['username']) is not None:
            return {'message': 'user with this username already exists'}, 400
        if User.get_by_email(data['email']) is not None:
            return {'message': 'user with this email already exists'}, 400
        User(data['username'], generate_password_hash(data['password']), data['email']).add_user()
        try:
            r = requests.post('http://mail:5005/registermail',
                              headers={
                                  'username': data['username']
                              })
        finally:
            return {'message': 'user registered successfully'}, 201


class Login(Resource):
    def post(self):
        data = request.get_json()
        if data.get('username') is None or data.get('username') is None:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(data['username'])
        if user and check_password_hash(user.password, data['password']):
            key = current_app.config['PRIVATE_KEY']
            now = datetime.datetime.utcnow().timestamp()
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


class ValidateToken(Resource):
    def post(self):
        key = current_app.config['PUBLIC_KEY']
        token = request.headers.get('JWT-token')
        audience = request.headers.get('audience')
        if token is None or audience is None:
            return {'is_valid': False}, 400
        if rd.get(token) is not None:
            return {'is_valid': False}, 400
        try:
            decoded = jwt.decode(token, key, audience=audience, issuer='https://motomotoorsthlikethat.com', algorithm='RS512')
        except (jwt.ExpiredSignatureError, jwt.InvalidAlgorithmError, jwt.InvalidAudienceError, jwt.InvalidIssuerError,
                jwt.InvalidTokenError, jwt.InvalidSignatureError, jwt.InvalidIssuedAtError):
            return {'is_valid': False}, 400
        if decoded['iat'] < User.get_by_username(audience).registerdate.timestamp():
            return {'is_valid': False}, 400
        return {'is_valid': True}, 201


class Delete(Resource):
    @authrequired
    def delete(self):
        user = User.get_by_username(request.headers.get('audience'))
        user.delete_user()
        return {'message': 'user deleted successfully'}, 201


class RevokeToken(Resource):
    @authrequired
    def post(self):
        token = request.headers.get('JWT-token')
        rd.set(token, '1', ex=60*60*48)
        rd.bgsave()
        return {'message': 'token revoked successfully'}, 201
