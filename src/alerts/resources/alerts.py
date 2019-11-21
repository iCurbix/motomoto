from flask_restful import Resource, request
from src.models.alert import AlertModel
from src.models.user import User
from src.utils.checkauth import authrequired


class Alert(Resource):
    @authrequired
    def put(self):
        data = request.get_json()
        if data is None:
            return {'message': 'data not correct'}, 400
        username = request.headers.get('audience')
        if None in [data.get('alerts'), username]:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(username)
        for alertdata in data.get('alerts'):
            if None in [user.id, alertdata.get('product'), alertdata.get('price')]:
                return {'message': 'data not correct'}, 400
            alert = AlertModel(user.id, alertdata.get('product'), alertdata.get('price'))
            alert.add_alert()
        return {'message': 'alerts added succesfully'}, 201

    @authrequired
    def delete(self):
        data = request.get_json()
        if data is None:
            return {'message': 'data not correct'}, 400
        username = request.headers.get('audience')
        if None in [data.get('alerts'), username]:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(username)
        for alert in [AlertModel.get_alert_by_id(_id) for _id in data['alerts']]:
            if alert is None:
                continue
            if alert.user != user.id:
                return {'message': "you cannot delete alerts that aren't yours"}, 401
            alert.delete_alert()
        return {'message': 'deleted successfully'}, 201

    @authrequired
    def patch(self):
        data = request.get_json()
        if data is None:
            return {'message': 'data not correct'}, 400
        username = request.headers.get('audience')
        if None in [username, data.get('alerts')]:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(username)
        for alertdict in data.get('alerts'):
            if None in [alertdict.get('id'), alertdict.get('product'), alertdict.get('price')]:
                return {'message': 'data not correct'}, 400
            alert = AlertModel.get_alert_by_id(alertdict['id'])
            if alert is None:
                return {'message': 'data not correct'}, 400
            if user.id != alert.user:
                return {'message': "you cannot change alerts that aren't yours"}, 401
            alert.update_info(alertdict['product'], alertdict['price'])
        return {'message': 'updated successfully'}

    @authrequired
    def get(self):
        data = request.get_json()
        if data is None:
            return {'message': 'data not correct'}, 400
        username = request.headers.get('audience')
        if None in [username, data.get('alerts')]:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(username)
        alerts = []
        for alertid in data.get('alerts'):
            alert = AlertModel.get_alert_by_id(alertid)
            if alert is None:
                continue
            if user.id != alert.user:
                return {'message': 'you can get only your own alerts'}, 401
            alerts.append(alert)
        return {'alerts': AlertModel.list_to_dict(alerts)}, 201


class Alerts(Resource):
    @authrequired
    def get(self, username):
        if not username == request.headers.get('audience'):
            return {'message': 'you can get only your own alerts'}, 400
        user = User.get_by_username(username)
        alerts = AlertModel.get_alerts_by_user_id(user.id)
        return {'alerts': AlertModel.list_to_dict(alerts)}, 201


class ChangeActive(Resource):
    @authrequired
    def post(self):
        data = request.get_json()
        if data is None:
            return {'message': 'data not correct'}, 400
        username = request.headers.get('audience')
        if None in [username, data.get('alerts')]:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(username)
        for alertid in data.get('alerts'):
            alert = AlertModel.get_alert_by_id(alertid)
            if alert is None:
                continue
            if user.id != alert.user:
                return {'message': 'you can modify only your own alerts'}, 401
            alert.change_active()
        return {'message': 'updated active states successfully'}, 201
