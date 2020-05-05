from flask import Flask
from flask import send_file,current_app
import enaduNew
import time
import os
import dirve
import fire
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
	return "Download Paper from this app-><br><a href=https://play.google.com/store/apps/details?id=com.sdnews.epapers&hl=en>link</a>"
	date=time.strftime("%d-%m-%Y")
	link=fire.get_firebase(date,flid)
	if (link!=None):
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a><br>"
	else:
		enaduNew.downloadPaper(flid,flname,quality)
		link=dirve.getLink(flname+".pdf")
		fire.set_firebase(date,flid,link)
		os.remove(flname+".pdf")
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a>"

#app.run()