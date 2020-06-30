#!/venv/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return { 'message': 'Hello World' }


class HelloSome(Resource):
    def get(self, some):
        return { 'message': f'Hello {some}' }


api.add_resource(HelloWorld, '/')
api.add_resource(HelloSome, '/<string:some>')


if __name__ == '__main__':
    app.run(port='9000')
