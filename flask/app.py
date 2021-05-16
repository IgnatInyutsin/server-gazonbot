import os
from flask import Flask, jsonify, request
import secondStage
app = Flask(__name__)

#функция handler срабатывает, если запрос идет на корень
@app.route('/', methods=['GET'])
def handler():
    return secondStage.secondStage()

if __name__ == '__main__':
    app.run(host='0.0.0.0')