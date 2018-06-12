from flask import Flask
from flask import request
from flask import render_template
from flask import url_for

app = Flask(__name__)



@app.route("/")
def hello():
        name = 'its a name'
	return render_template('index.html',name=name)

@app.route("/home",methods=['GET','POST'])
def home():
	if request.method == 'POST':
		return "sfd"	
	else:
		return "<h2>Welcome</h2>"
