from flask import Flask, jsonify, request
import os
import mailActions
import messageParsing

app = Flask(__name__)

credentials = {
    "username": os.environ['MY_USER'],
    "password": os.environ['MY_PASS'],
    "imap": 'imap.gmail.com',
    "smtp": "smtp.gmail.com"
}


@app.route('/run')
def run():
    input = request.args.get('command', default="*", type=str)
    command = input.replace("%20", " ")
    parsed = messageParsing.parse(command)
    mailActions.sendMail(credentials, "gray.lott@gmail.com", parsed.subject, parsed.body)
    print("Mail Found, Processing")
    return "Message Sent"