import requests
from PIL import Image
from io import BytesIO
import os
import threading
import time

class EenaduEpaper:
	def __init__(self,no):
		self.id=no

	def allPageDetails(self):
		res=requests.get("https://epaper.eenadu.net/Home/GetAllpages?editionid="+str(self.id)+"&editiondate="+time.strftime("%d")+"%2F"+time.strftime("%m")+"%2F"+time.strftime("%Y"),timeout=8000).json()
		data=[]
		for i in res:
			data.append(i["XHighResolution"])
		return data

	def formCompleteImg(url):
		headers={'Referer': 'https://epaper.eenadu.net/Home/Index', 'Sec-Fetch-Mode': 'no-cors', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
		url1=url
		url2=url[:-3]+'png'
		img = Image.open(BytesIO(requests.get(url2,headers=headers,timeout=8000).content)).convert("RGBA")
		background = Image.open(BytesIO(requests.get(url1,headers=headers,timeout=8000).content))
		background.paste(img, (0, 0), img)
		return background

	def DownloadPaper(self):
		arr=[]
		for i in self.paperJson:
			t=threading.Thread(target=self.formCompleteImg,args=(self.paperJson[i]["levels"]["level2"]["chunks"],int(i)))
			arr.append(t)
			t.start()
		no=1
		for i in arr:
			print(no)
			no+=1
			i.join()
		img=self.emptyImage[0]
		self.emptyImage.pop(0)
		img.save('sam.pdf',save_all=True, append_images=self.emptyImage)

data=allPageDetails(1)
print(data)
for i in data:
	formCompleteImg(i).show()
	break