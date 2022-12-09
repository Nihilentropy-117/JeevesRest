from flask import Flask, jsonify, request
import os

app = Flask(__name__)

username = os.environ['MY_USER']
password = os.environ['MY_PASS']


@app.route('/user')
def get_incomes():
    incomes = ("Running with user: %s" % username)
    return incomes


