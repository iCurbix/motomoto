import requests
from functools import wraps
from flask import request
from src.models.user import User


def authrequired(func):
    @wraps(func)
    def checkjwt(*args, **kwargs):
        token = request.headers.get('JWT-token')
        audience = request.headers.get('audience')
        if User.get_by_username(audience) is None:
            return {'message': 'user does not exist'}, 400
        if token is None or audience is None:
            return {'message': 'did not receieve token'}, 401
        try:
            r = requests.post('http://auth:5001/validate',
                              headers={
                                  'JWT-Token': token,
                                  'audience': audience,
                              })
        except requests.exceptions.RequestException as e:
            return {'message': e}, 401
        if not r.json().get('is_valid', False):
            return {'message': 'invalid token'}, 401
        return func(*args, **kwargs)
    return checkjwt
