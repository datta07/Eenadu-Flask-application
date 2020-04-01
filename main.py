from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
	return "datta welcomes you all guys"

@app.route('/today')
def today():
	return time.strftime("%T")