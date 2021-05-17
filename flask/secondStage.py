import os
from flask import Flask, jsonify, request
import app
import psycopg2
import sys
sys.path.insert(1, 'methods/')
import lowCharge

#тут будут последующие действия
def secondStage(data):
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

	#запускаем миграции. Если уже были - ставьте значение ниже False
	runMigrations = False

	if runMigrations == True:
		#собираем список с именами файлов
		files = os.listdir("migration/")
		for file in range(len(files)):
			#сюда вносите изменения о работе отдельных миграций
			#собираем список со строками миграции
			migration = open('migration/' + files[file], 'r').readlines()
			#собираем в один файл
		
			result = ""
			for line in range(len(migration)):
				result += migration[line] + " "
		
			#добавляем
			cursor.execute(result)

	db.commit()

	#третий этап - много разветвлений, связанных с методом
	#массив со всеми обработчиками
	#reasons = ["lowCharge", "leadFree"]
	#for reason in range(len(reasons)):
	#	if data["reason"] == reasons[reason]:
	#		return exec(reasons[reason] + "main(data)")

	return "IDK"