from datetime import datetime
from appName import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(120), unique=True, nullable=False)

	def __repr__(self):
		return f"User('{self.email}', '{self.id})"

class Address(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user = db.Column(db.String(60), unique=True, nullable=False)
	address = db.Column(db.String(120), unique=True, nullable=False)

	def __repr__(self):
		return f"Address('{self.user}', '{self.addres}')"


