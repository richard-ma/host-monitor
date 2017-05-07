import json
from flask import request, abort
from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from . import app, api, mongo

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

        jo = json.loads(args['host'])
        host_id = mongo.db.hosts.insert(jo)
        return monngo.db.hosts.find_one({"_id": host_id})

class Host(Resource):
    def get(self, host_id):
        return mongo.db.hosts.find_one_or_404({"_id": host_id})

    def delete(self, host_id):
        mongo.db.hosts.find_one_or_404({"_id": host_id})
        mongo.db.hosts.remove({"_id": host_id})
        return '', 204

class Root(Resource):
    def get(self):
        return {
                'status': 'OK',
                'mongo': str(mongo.db),
                }

api.add_resource(Root, '/')
api.add_resource(HostList, '/hosts/')
api.add_resource(Host, '/hosts/<ObjectId:host_id>')
