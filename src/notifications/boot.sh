#!/bin/sh
source venv/bin/activate
flask db init
exec python src/notifications/app.py