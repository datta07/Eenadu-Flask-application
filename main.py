from flask import Flask
from flask import send_file
import time

app = Flask(__name__)

@app.route('/')
def home():
	return "datta Akula welcomes you all guys"

@app.route('/today')
def today():
	return time.strftime("%T")

@app.route('/show-pdf')
def show_static_pdf():
	file=open("k.pdf","rb")
	return send_file(file,attachment_filename="kr.pdf")

app.run()