import json
from datetime import datetime
from flask import request, abort
from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from . import app, api, mongo
from ./helper import get_client_ip

class HostList(Resource):
    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('host', type=str)

        super(HostList, self).__init__()

    def get(self):
        return [x for x in mongo.db.hosts.find()]

    def post(self):
        args = self.parser.parse_args()
        if not args['host']:
            abort(400)

        host = dict()
        host['name'] = args['host']
        host['ip'] = get_client_ip(request)
        host['last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        host_id = mongo.db.hosts.insert_one(host).inserted_id
        return mongo.db.hosts.find_one({"_id": host_id})

class Host(Resource):
    def get(self, host_name):
        return mongo.db.hosts.find_one_or_404({"name": host_name})

    def put(self, host_name):
        mongo.db.hosts.find_one_or_404({"name": host_name})

        host = dict()
        host['name'] = host_name
        host['ip'] = get_client_ip(request)
        host['last_update'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        mongo.db.hosts.update_one({"name": host_name}, {"$set": host})
        return mongo.db.hosts.find_one_or_404({"name": host_name})


    def delete(self, host_name):
        mongo.db.hosts.find_one_or_404({"name": host_name})
        mongo.db.hosts.remove({"name": host_name})
        return '', 204

class Root(Resource):
    def get(self):
        return {'status': 'OK'}

api.add_resource(Root, '/')
api.add_resource(HostList, '/hosts/')
api.add_resource(Host, '/hosts/<string:host_name>/')
