import json

def set_values(date,value,link):
	data=json.loads(open("data.json","r").read())
	data[date]={value:link}
	with open('data.json', 'w') as f:
		json.dump(data, f)

def get_value(date,value):
	data=json.loads(open("data.json","r").read())
	try:
		return data[date][value]
	except Exception:
		return False

def data():
	data=json.loads(open("data.json","r").read())
	return str(data)

