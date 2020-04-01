from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "datta welcomes you all guys"
