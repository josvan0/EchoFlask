#!/venv/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api, Resource


# initialize a Flask app (a server)
app = Flask(__name__)
# implements the Api class on the app
api = Api(app)


# create a resource api with Resource class
class Hello(Resource):
    # define method GET with keyword params (optionals)
    def get(self, some=None):
        # return object Python as JSON
        return {
            'message': f'Hello {some}'
        } if some else {
            'message': 'Hello World'
        }


# add the resource to api
# resource it's used to paths specified
api.add_resource(Hello, '/', '/<string:some>', endpoint='hello')


if __name__ == '__main__':
    # start server on port selected
    app.run(port='9000')
