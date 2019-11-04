from flask_sqlalchemy import SQLAlchemy
from writer import app, db

class Person(db.Model):
	__tablename__ = "Person"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	country = db.Column(db.String(30))

	def __init__(self, name, country):
		self.name = name
		self.country = country

	def __repr__(self):
		return f"Person('{self.id}', '{self.name}', '{self.country}')"

