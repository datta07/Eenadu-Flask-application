from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def home():
	return "datta Akula welcomes you all guys"

@app.route('/today')
def today():
	return time.strftime("%T")