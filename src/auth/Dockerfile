FROM python:3.8-alpine

RUN adduser -D motomotoauth

WORKDIR /home/motomotoauth

COPY src/auth/requirements.txt requirements.txt
RUN apk add build-base
RUN apk add postgresql-dev
RUN apk add --no-cache libressl-dev musl-dev libffi-dev
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

RUN venv/bin/pip install flask_cors

RUN mkdir src
COPY boot.sh boot.sh
COPY src/__init__.py src/__init__.py
COPY src/db.py src/db.py
COPY src/redisdb.py src/redisdb.py
COPY src/config.py src/config.py
COPY src/auth src/auth
COPY src/utils src/utils
COPY src/models src/models
RUN chmod +x boot.sh

RUN chown -R motomotoauth:motomotoauth ./
USER motomotoauth

EXPOSE 5001
ENTRYPOINT ["./boot.sh"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]