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

@app.route('/santhi-pdf/<flid>/<flname>/<quality>', methods=['GET', 'POST'])
def download(flid,flname,quality):
	date=time.strftime("%d-%m-%Y")
	link=fire.get_firebase(date,flid)
	if (link!=None):
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a><br>To Download other Papers from this app-><br><a href=https://play.google.com/store/apps/details?id=com.sdnews.epapers&hl=en>link</a>"
	else:
		enaduNew.downloadPaper(flid,flname,quality)
		link=dirve.getLink(flname+".pdf")
		fire.set_firebase(date,flid,link)
		os.remove(flname+".pdf")
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a><br>To Download other Papers from this app-><br><a href=https://play.google.com/store/apps/details?id=com.sdnews.epapers&hl=en>link</a>"

@app.route('/Eenadu-pdfs/<flid>/<flname>/<quality>', methods=['GET', 'POST'])
def download1(flid,flname,quality):
	date=time.strftime("%d-%m-%Y")
	link=fire.get_firebase(date,flid)
	if (link!=None):
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a><br>To Download other Papers from this app-><br><a href=https://play.google.com/store/apps/details?id=com.telugudaily.downloader>link</a>"
	else:
		enaduNew.downloadPaper(flid,flname,quality)
		link=dirve.getLink(flname+".pdf")
		fire.set_firebase(date,flid,link)
		os.remove(flname+".pdf")
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a><br>To Download other Papers from this app-><br><a href=https://play.google.com/store/apps/details?id=com.telugudaily.downloader&hl=en>link</a>"

@app.route('/Epdf/<flid>/<flname>/<quality>', methods=['GET', 'POST'])
def download2(flid,flname,quality):
	date=time.strftime("%d-%m-%Y")
	link=fire.get_firebase(date,flid)
	if (link!=None):
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a><br>To Download other Papers from this app-><br><a href=https://play.google.com/store/apps/details?id=com.teluguenewspaperspdf.dailynewspaper&hl=en>link</a>"
	else:
		enaduNew.downloadPaper(flid,flname,quality)
		link=dirve.getLink(flname+".pdf")
		fire.set_firebase(date,flid,link)
		os.remove(flname+".pdf")
		return "download "+flname+"<br>Download: <a href="+link+">clickHere</a><br>To Download other Papers from this app-><br><a href=https://play.google.com/store/apps/details?id=com.teluguenewspaperspdf.dailynewspaper&hl=en>link</a>"

#app.run()