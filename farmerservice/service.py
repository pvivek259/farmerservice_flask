from flask import Flask, app
from flask_restful import Api
from flask import jsonify
from handler.testHandler import TestHelloWorld
from handler.farmerHandler import FarmerHandler
from handler.shippingAddressHandler import ShippingAddressHandler

app = Flask(__name__)
api = Api(app)


api.add_resource(TestHelloWorld, '/testHello')
api.add_resource(FarmerHandler, '/farmer')
api.add_resource(ShippingAddressHandler, '/shippingAddress')

@app.route('/test')
def index():
    return jsonify({'message': 'success',
                    'email': 'Yes i am wokring'})

app.run()