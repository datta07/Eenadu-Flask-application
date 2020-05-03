from flask import Flask
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
    with open('k.pdf', 'rb') as static_file:
        return send_file(static_file, attachment_filename='file.pdf')