from flask import Flask
from flask import send_file,current_app
import time

app = Flask(__name__)

@app.route('/')
def home():
	return "datta Akula welcomes you all guys"

@app.route('/today')
def today():
	return time.strftime("%T")

@app.route('/show-pdf', methods=['GET', 'POST'])
def download():
	path = "k.pdf"
	return send_file(path, as_attachment=True)

#app.run()