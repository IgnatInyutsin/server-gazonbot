import os
from flask import Flask, jsonify, request
from . import *
import psycopg2

#тут будут последующие действия
secondStage(data):
	db = psycopg2.connect(
		database="gazonbot_db",
		user="gazonbot_user",
		password="PaSsWoRd21",
		host="127.0.0.1",
		port="5432"
	)
	return "ВААААЙ МАЛАДЕССССС"