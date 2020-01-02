FROM python:3.8-alpine

RUN adduser -D motomotosearch

WORKDIR /home/motomotosearch

COPY src/search/requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

RUN mkdir src
COPY boot.sh boot.sh
COPY src/__init__.py src/__init__.py
COPY src/search src/search
COPY src/utils src/utils
RUN chmod +x boot.sh

RUN chown -R motomotosearch:motomotosearch ./
USER motomotosearch

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]