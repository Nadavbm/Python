from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@192.168.178.91/myapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)

	def __init__(self, username, email):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username 

db.init_app(app)
db.create_all()
db.session.commit()

nadav = User('nadav', 'nadav@example.com')

db.session.add(nadav)
db.session.commit()

if __name__ == "__main__":
	app.run(host='0.0.0.0')

