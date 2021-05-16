import os
from flask import Flask, jsonify, request
import app
import psycopg2

#тут будут последующие действия
def secondStage():
	#подключение к бд
	db = psycopg2.connect(
		database="gazonbot_db",
		user="gazonbot_user",
		password="PaSsWoRd21",
		host="pg_db",
		port="5432"
	)
	
	#устанавливаем курсор
	cursor = db.cursor()

	#если нет таблиц - создаем
	cursor.execute('''
	CREATE TABLE IF NOT EXISTS "user"
	(id SERIAL NOT NULL PRIMARY KEY,
	email VARCHAR(320) NOT NULL,
	hashpass VARCHAR(160) NOT NULL);

	CREATE TABLE IF NOT EXISTS "session"
	(session_id VARCHAR(128) NOT NULL,
	user_id INT NOT NULL,
	expires BIGINT NOT NULL);
	
	CREATE TABLE IF NOT EXISTS "group"
	(id SERIAL NOT NULL PRIMARY KEY,
	user_id INT,
	status_id INT NOT NULL,
	width FLOAT,
	length FLOAT);

	CREATE TABLE IF NOT EXISTS robot
	(id SERIAL NOT NULL PRIMARY KEY,
	group_id INT,
	user_id INT,
	type_id INT NOT NULL,
	token VARCHAR(255) NOT NULL);

	CREATE TABLE IF NOT EXISTS robot_type
	(id SERIAL NOT NULL PRIMARY KEY,
	name VARCHAR(24));
	''')

	#измените данный параметр чтобы связи не обновлялись
	changeQuestion = True

	if changeQuestion == True:
	#пишем связи
		cursor.execute('''
		SELECT "user", "group"	
		FROM "group" 
		JOIN "user" ON "group".user_id = "user".id
		''')

		cursor.execute('''
		SELECT "user", "session"
		FROM "session"
		JOIN "user" ON "session".user_id = "user".id
		''')

		cursor.execute('''
		SELECT robot, "group"
		FROM robot 
		JOIN "group" ON robot.group_id = "group".id
		''')

		cursor.execute('''
		SELECT robot, "user"
		FROM robot 
		JOIN "user" ON robot.user_id = "user".id
		''')

		cursor.execute('''
		SELECT robot, robot_type
		FROM robot
		JOIN robot_type ON robot.type_id = robot_type.id
		''')

	#отправляем изменения
	db.commit()
	#сам вывод
	return jsonify({"da...": "lol"})