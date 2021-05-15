import os
from flask import Flask, jsonify, request
from . import *
app = Flask(__name__)

#функция handler срабатывает, если запрос идет на корень
@app.route('/', methods=['GET'])
def handler():
    if decodingTest(request.form["secret_code"]):
        return secondStage(request.form)
    else:
        return "ПАШЕЛ НАХУЙ ГРЯЗНЫЙ ХАКЕР ЫАЫАЫА"