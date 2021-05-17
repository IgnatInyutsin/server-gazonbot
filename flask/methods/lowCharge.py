import psycopg2

def main(data):
	db = psycopg2.connect(
		database="gazonbot_db",
		user="gazonbot_user",
		password="PaSsWoRd21",
		host="pg_db",
		port="5432"
	)

	cursor = db.cursor()
	#запрос
	cursor.execute('''
	SELECT robot.id WHERE robot.id = ${data[author]}
	''')

	if cursor.fetchall() == data[author]:
		cursor.execute('''
		SELECT robot.id, robot.status_id
		UPDATE robot SET status_id=5 WHERE robot.id=${data[author]}
		''')