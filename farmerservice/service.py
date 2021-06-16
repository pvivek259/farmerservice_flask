from farmerservice_flask.farmerservice.handler.shippingAddressHandler import ShippingAddressHandler
from farmerservice_flask.farmerservice.handler.farmerHandler import FarmerHandler, GetFarmer
from flask import Flask, app
from flask_restful import Api
from flask import jsonify

app = Flask(__name__)
api = Api(app)


api.add_resource(FarmerHandler, '/farmer')
api.add_resource(GetFarmer, '/getfarmer')
api.add_resource(ShippingAddressHandler, '/shippingAddress')



app.run()