import requests
from PIL import Image
from io import BytesIO
import os
import threading
from lxml import html

class readwhere:
	def __init__(self,url,folder,name):
		self.paperJson = requests.get(url).json()
		self.folder=folder
		try:
			os.mkdir(folder)
		except Exception:
			pass
		self.name=name
		self.dim=[int(self.paperJson["1"]["levels"]["level2"]["width"]),int(self.paperJson["1"]["levels"]["level2"]["height"])]
		self.emptyImage=[]
		for i in self.paperJson:
			self.emptyImage.append(None)

	def formCompleteImg(self,url):
		url1=url
		url2=url[:-3]+'png'
		img = Image.open(BytesIO(requests.get(url2).content)).convert("RGBA")
		background = Image.open(BytesIO(requests.get(url1).content))
		background.paste(img, (0, 0), img)
		return background

	def makeEmptyPage(self):
		return Image.new('RGB',self.dim,'white')

	def addImgToEmpty(self,data,no):
		if (self.emptyImage[no-1]==None):
			self.emptyImage[no-1]=self.makeEmptyPage()
		self.emptyImage[no-1].resize((int(data["width"]),int(data["height"])))
		if (data['url'][-3:]=='png'):
			return
		else:
			self.emptyImage[no-1].paste(self.formCompleteImg(data["url"]),(int(data["tx"]),int(data["ty"])))

	def formPage(self,Paperdata,no):
		for i in Paperdata:
			self.addImgToEmpty(i,no)
		self.emptyImage[no-1].convert("RGB")

	def DownloadPaper(self):
		arr=[]
		for i in self.paperJson:
			t=threading.Thread(target=self.formPage,args=(self.paperJson[i]["levels"]["level2"]["chunks"],int(i)))
			arr.append(t)
			t.start()
		no=1
		for i in arr:
			print(no)
			no+=1
			i.join()
		img=self.emptyImage[0]
		self.emptyImage.pop(0)
		img.save(self.folder+'/'+self.name+'.pdf',save_all=True, append_images=self.emptyImage)

def getTodayId(k):
	with requests.Session() as s:
	    r=s.get('https://epaper.sakshi.com/t/'+str(k))
	    k=r.content
	    k=k.decode('utf-8')

	tree = html.fromstring(k)
	k=tree.xpath('//div[@class="section_publication"]//a')
	k=k[0].values()
	k=(k[0].split('/'))[-1]
	return k

def get_network(path):
	print('connecting to internet .....')
	url1='https://test-bfdc9.firebaseio.com/'+path+'/.json'
	if path=='':
		url1='https://test-bfdc9.firebaseio.com/.json'
	auth_key = 'yGTJKpUSKfdIznLem10KAK4dm2fqKHSNMJEzagfh'
	try:
		r1=requests.get(url1 + '?auth=' + auth_key)
		return r1.json()
	except Exception as e:
		print('no internet')
		return 0
def downloadPaper(id):
	obj=readwhere("https://epaper.sakshi.com/pagemeta/get/"+getTodayId(id)+"/1-50",'.','file')
	obj.DownloadPaper()