from flask_restful import Resource, Api

class TestHelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'hello': 'post world'}

    def put(self):
        return {'hello': 'put world'}