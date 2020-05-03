from flask import Flask
from flask import send_file,current_app
import sak
import time
import os

app = Flask(__name__)

@app.route('/')
def home():
	return "datta aula welcomes you all guys"

@app.route('/today')
def today():
	return time.strftime("%T")

@app.route('/sh-pdf/<flid>/<flname>', methods=['GET', 'POST'])
def download(flid,flname):
	sak.downloadPaper(flid)
	path = "file.pdf"
	return send_file(path,as_attachment=True,attachment_filename=flname+'.pdf')

#app.run()