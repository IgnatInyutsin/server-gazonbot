import os
from flask import Flask, jsonify
app = Flask(__name__)

#we define the route /
@app.route('/')
def welcome():
    # return a json
    return jsonify({'status': 'api working'})