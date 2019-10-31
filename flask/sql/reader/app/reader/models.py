from flask_sqlalchemy import SQLAlchemy
from reader import db

class Address(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), unique=False)
	street = db.Column(db.String(30), unique=False)
	number = db.Column(db.Integer, unique = False)
	city = db.Column(db.String(30), unique = False)
	country = db.Column(db.String(30), unique = False)

	def __repr__(self):
		return f"Address('{self.id}', '{self.name}', '{self.street}', '{self.number}', '{self.city}', '{self.country}')"

"""
	def __repr__(self):
		return "<Address(id='%d', street='%s', number='%d', city='%s', country='%s')>" % (self.id, self.street, self.number, self.city, self.country)

	def __repr__(self):
		return '[%r, %r, %r, %r, %r]' % (self.id, self.street, self.number, self.city, self.country)	
"""
