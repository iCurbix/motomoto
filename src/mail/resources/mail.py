import smtplib
import ssl
from flask_restful import Resource
from flask import request, render_template, current_app
from src.models.user import User
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


senderemail = 'motomotoflask@gmail.com'


def sendmail(sender, receiver, subject, text, html):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(current_app.config['MAIL_SERVER'], current_app.config['MAIL_PORT'], context=context) as server:
        server.login(current_app.config['MAIL_USERNAME'], current_app.config['MAIL_PASSWORD'])
        server.sendmail(
            sender, receiver, message.as_string()
        )


class RegisterMail(Resource):
    def post(self):
        data = request.headers
        if data.get('username') is None:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(data.get('username'))
        if user is None:
            return {'message': 'data not correct'}, 400
        text = render_template('mail/register_mail_template.txt', user=user)
        html = render_template('mail/register_mail_template.html', user=user)
        sendmail(senderemail, user.email, 'Welcome to motomoto!', text, html)
        return {'message': 'register mail sent successfully'}, 201


class AlertMail(Resource):
    def post(self):
        headers = request.headers
        data = request.get_json()
        if data.get('products') is None:
            return {'message': 'data not correct'}, 400
        if headers.get('username') is None:
            return {'message': 'data not correct'}, 400
        user = User.get_by_username(headers.get('username'))
        if user is None:
            return {'message': 'data not correct'}, 400
        text = render_template('mail/alert_mail_template.txt', user=user, products=data.get('products'))
        html = render_template('mail/alert_mail_template.html', user=user, products=data.get('products'))
        sendmail(senderemail, user.email, 'Price alerts from motomoto', text, html)
        return {'message': 'alert mail sent successfully'}, 201
