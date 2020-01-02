FROM python:3.8-alpine

RUN adduser -D motomotomail

WORKDIR /home/motomotomail

COPY src/mail/requirements.txt requirements.txt
RUN apk add build-base
RUN apk add postgresql-dev
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

RUN mkdir src
COPY boot.sh boot.sh
COPY src/__init__.py src/__init__.py
COPY src/db.py src/db.py
COPY src/config.py src/config.py
COPY src/mail src/mail
COPY src/utils src/utils
COPY src/models src/models
COPY templates templates
RUN chmod +x boot.sh

RUN chown -R motomotomail:motomotomail ./
USER motomotomail

EXPOSE 5005
ENTRYPOINT ["./boot.sh"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]