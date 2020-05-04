import json

def set_values(date,value,link):
	with open("data.json","r") as f:
		data=json.loads(f.read())
	if date in data:
		data[date][value]=link
	else:
		data[date]={value:link}
	with open('data.json','w') as f:
		json.dump(data, f)

def get_value(date,value):
	with open("data.json","r") as f:
		data=json.loads(f.read())
	try:
		return data[date][value]
	except Exception:
		return False

def data():
	with open("data.json","r") as f:
		data=json.loads(f.read())
	return str(data)