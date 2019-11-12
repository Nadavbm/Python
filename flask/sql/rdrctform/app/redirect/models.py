from flask_sqlalchemy import SQLAlchemy
from redirect import app, db

class User(db.Model):
	__tablename__ = "User"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50))
	email = db.Column(db.String(50))

	def __init__(self, username, email):
		self.username = username
		self.email = email

	def __repr__(self):
		return f"User('{self.id}', '{self.username}', '{self.email}')" 


