from flask import Flask
from flask import request
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'credentials'
app.config['MYSQL_HOST'] = 'db_container'
mysql = MySQL(app)

@app.route('/person', methods=['POST'])
@app.route('/person/', methods=['POST'])
def insert():
	first_name = request.form.get('firstname')
	last_name = request.form.get('lastname')

	dbConnection = mysql.connect
	dbCursor = dbConnection.cursor()

	dbCursor.execute("INSERT INTO credentialstable (FirstName, LastName) VALUES ('" + 
			first_name + "','" + last_name + "')")
	dbConnection.commit()

	return 'Halla bel'

@app.route('/persons', methods=['GET'])
@app.route('/persons/', methods=['GET'])
def get():
	dbConnection = mysql.connect
	dbCursor = mysql.connection.cursor()
	dbCursor.execute("SELECT * FROM credentialstable")
	rv = dbCursor.fetchall()
	jsonData = []
	for result in rv:
		jsonData.append({'PersonID':result[0], 'Firstname':result[1], 'Lastname':result[2]})
	dbCursor.close()
	return json.dumps(jsonData)


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
