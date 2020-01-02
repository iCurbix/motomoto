#!/bin/sh
source venv/bin/activate
flask db init
exec gunicorn -b :$APPPORT --workers 4 --access-logfile - --error-logfile - $APPROUTE