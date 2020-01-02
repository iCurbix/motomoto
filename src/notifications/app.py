from flask import Flask
from flask_migrate import Migrate
from src.config import Config
from src.models.alert import AlertModel
from src.models.user import User
import schedule
import time
import requests
import itertools
import logging
import sys
from src.db import db


log = logging.getLogger(__name__)
out_hdlr = logging.StreamHandler(sys.stderr)
out_hdlr.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
out_hdlr.setLevel(logging.INFO)
log.addHandler(out_hdlr)
log.setLevel(logging.INFO)

app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)

db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()


def job():
    with app.app_context():
        log.info('Checking alerts')
        allalerts = AlertModel.list_to_dict(AlertModel.get_all_active_alerts())
        allalerts = sorted(allalerts, key=lambda x: x['user'])
        allalerts = itertools.groupby(allalerts, lambda x: x['user'])

        for userid, alerts in allalerts:
            productlist = []
            alerts_to_deactivate = []

            for alert in alerts:
                r = requests.get(f'http://search:5000/{alert["product"]}')
                if r.status_code != 201:
                    continue
                productnum = len(productlist)

                for shop in r.json().values():
                    productlist += [product for product in shop['products'] if product['price'] <= alert['price']]

                if productnum != len(productlist):
                    alerts_to_deactivate.append(alert)

            if len(productlist) == 0:
                continue
            user = User.get_by_id(userid)
            log.info(f'Sending notifications to {user.username}')
            r2 = requests.post('http://mail:5005/alertmail',
                               headers={
                                   'Content-Type': 'application/json',
                                   'username': user.username
                               },
                               json={'products': productlist}
                               )

            if r2.status_code != 201:
                continue

            for alert in alerts_to_deactivate:
                AlertModel.get_alert_by_id(alert['id']).change_active()


schedule.every().hour.do(job)

if __name__ == '__main__':
    log.info('Starting app')
    while True:
        schedule.run_pending()
        time.sleep(1)
