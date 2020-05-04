from flask import Flask
from flask import send_file,current_app
import enaduNew
import time
import os
import dirve
import jsonController
import time
from flask_cors import CORS


os.environ['TZ']='Asia/Kolkata'
time.tzset()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
	return "datt aula welcomes you all guys"

@app.route('/today')
def today():
	return time.strftime("%T")

@app.route('/sh-pdf/<flid>/<flname>/<quality>', methods=['GET', 'POST'])
def download(flid,flname,quality):
	date=time.strftime("%d-%m-%Y")
	link=jsonController.get_value(date,flid)
	if (link):
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a><br>"+jsonController.data()
	else:
		enaduNew.downloadPaper(flid,flname,quality)
		link=dirve.getLink(flname+".pdf")
		os.remove(flname+".pdf")
		jsonController.set_values(date,flid,link)
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a>"+jsonController.data()

#app.run()