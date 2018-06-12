from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
#from json import dumps
from flask_jsonpify import jsonify
from flask_pymongo import PyMongo

import json
from bson import ObjectId

import config as config

app = Flask(__name__)

api = Api(app)

CORS(app)

#mongo = PyMongo(app)
app.config['MONGO_HOST'] = 'localhost'
app.config['MONGO_PORT'] = 27017
app.config['MONGO_DBNAME'] = 'pyflask'
mongo = PyMongo(app, config_prefix='MONGO')

# class for jsoning
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

@app.route("/",methods=['GET','POST'])
def hello():
        name = 'its a name'
	return render_template('index.html',name=name)
	#return config.hello()
	#return jsonify({'text':'Hello World!'})

@app.route("/home",methods=['GET','POST'])
def home():
	if request.method == 'POST':
		return "sfd"	
	else:
		return "<h2>Welcome</h2>"


@app.route("/user",methods=['POST'])
def user_detail():
	user = mongo.db.user.find({},{"name":1,"age":1,"address":1,"_id":1})
#	print jsonify(users="sf")
	listuser = list(user)
	print listuser
	#return jsonify(listuser)
	return JSONEncoder().encode(listuser)
