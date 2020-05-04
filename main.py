from flask import Flask
from flask import send_file,current_app
import sak
import time
import os
import dirve
import jsonController
import time

app = Flask(__name__)

@app.route('/')
def home():
	return "datta aula welcomes you all guys"

@app.route('/today')
def today():
	return time.strftime("%T")

@app.route('/sh-pdf/<flid>/<flname>', methods=['GET', 'POST'])
def download(flid,flname):
	date=time.strftime("%d-%m-%Y")
	link=jsonController.get_value(date,flid)
	if (link):
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a>"
	else:
		sak.downloadPaper(flid)
		link=dirve.getLink("file.pdf")
		jsonController.set_values(date,flid,link)
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a>"

#app.run()