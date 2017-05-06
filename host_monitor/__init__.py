import os
from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from flask import make_response
from bson.json_util import dumps

MONGODB_URI = os.environ.get('MONGODB_URI')

app = Flask(__name__)

app.config['MONGO_URI'] = MONGODB_URI
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = Api(app)
api.representations = DEFAULT_REPRESENTATIONS

from . import resources
