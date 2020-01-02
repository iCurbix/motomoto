FROM python:3.8-alpine

RUN adduser -D motomotonotifications

WORKDIR /home/motomotonotifications

COPY src/notifications/requirements.txt requirements.txt
RUN apk add build-base
RUN apk add postgresql-dev
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt

RUN mkdir src
COPY src/__init__.py src/__init__.py
COPY src/db.py src/db.py
COPY src/config.py src/config.py
COPY src/notifications src/notifications
COPY src/models src/models
RUN chmod +x src/notifications/boot.sh

RUN chown -R motomotonotifications:motomotonotifications ./
USER motomotonotifications

ENTRYPOINT ["./src/notifications/boot.sh"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]