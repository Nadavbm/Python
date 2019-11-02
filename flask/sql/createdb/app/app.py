from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

def connect_db():
	return sqlite3.connect('people.db')

@app.route('/')
def home():
	db_connection = connect_db()
	cursor = db_connection.execute('SELECT id, name FROM person;')
	people = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
	return render_template('home.html', people=people)


if __name__ == "__main__":
	app.run(host='0.0.0.0')
