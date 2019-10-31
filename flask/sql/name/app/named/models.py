from flask_sqlalchemy import SQLAlchemy
from named import db

class Name(db.Model):
	__tablename__ = "named"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f"Name('{self.id}', '{self.name}')"

