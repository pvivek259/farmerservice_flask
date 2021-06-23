from handler.shippingAddressHandler import ShippingAddressHandler
from handler.farmerHandler import FarmerHandler, GetFarmer
from flask import Flask, app
from flask_restful import Api
from flask import jsonify
app = Flask(__name__)
api = Api(app)


api.add_resource(FarmerHandler, '/farmer')
api.add_resource(GetFarmer, '/getfarmer')
api.add_resource(ShippingAddressHandler, '/shippingAddress')

@app.route('/test')
def index():
  return jsonify({"Yes, i am working."})

app.run(host='0.0.0.0', port="9005")
#comment added in dev-branch