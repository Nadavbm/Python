from flask_sqlalchemy import SQLAlchemy
from address import app, db

class Address(db.Model):
	__tablename__ = "Address"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30))
	street = db.Column(db.String(30))
	number = db.Column(db.Integer)
	city = db.Column(db.String(30))
	country = db.Column(db.String(30))

	def __init__(self, name, street, number, city, country):
		self.name = name
		self.street = street
		self.number = number
		self.city = city
		self.country = country

	def __repr__(self):
		return f"Address('{self.id}', '{self.name}', '{self.street}', '{self.number}', '{self.city}', '{self.country}')"

