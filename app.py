from flask import Flask, jsonify, request
import os
import mailActions

app = Flask(__name__)

credentials = {
    "username": os.environ['MY_USER'],
    "password": os.environ['MY_PASS'],
    "imap": 'imap.gmail.com',
    "smtp": "smtp.gmail.com"
}


@app.route('/run')
def run():
    command = request.args.get('command', default="*", type=str)
    mailActions.sendMail(credentials, "gray.lott@gmail.com", "test", command)
    print("Mail Found, Processing")
