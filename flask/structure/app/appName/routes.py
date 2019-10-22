from flask import Flask, render_template, url_for, flash, redirect
from appName import app, db
from appName.forms import RegForm, LoginForm
from appName.models import User, Address
import sqlite3


def connect_db():
	return sqlite3.connect('some.db')

@app.route('/')
def home():
	db_connection = connect_db()
	cursor = db_connection.execute('select * from address')
	return render_template('index.html', items=cursor.fetchall())

@app.route('/about')
def about():
	return render_template('about.html')


