from flask import Flask, jsonify, request

app = Flask(__name__)

incomes = "potato"


@app.route('/incomes')
def get_incomes():
    return incomes


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204