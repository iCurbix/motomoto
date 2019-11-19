from flask_restful import Resource, request
from src.models.alert import AlertModel
from src.models.user import User
from src.utils.checkauth import authrequired


class Alert(Resource):
    @authrequired
    def post(self):
        pass


class Alerts(Resource):
    def get(self):
        pass
