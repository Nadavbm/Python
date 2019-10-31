from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from reader.models import Address 
from reader import app, db

@app.route('/')
def home():
	address = Address.query.all()
	return render_template('index.html', address=address)

