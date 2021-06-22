from flask import request
from views.shippingController import add_shipping_address, get_shipping_address
from flask_restful import Resource
from utils.errors import ErrorHandler

class ShippingAddressHandler(Resource):
    #post address by number
    def post(self):
        request_data = request.get_json(force=True)
        resp = add_shipping_address(request_data)
        return resp
      
      #get address by number
    def get(self):
        request_data = request.args
        try:
          resp = get_shipping_address(request_data)
        except ErrorHandler as e:
          return e.to_resp()

        return resp
        