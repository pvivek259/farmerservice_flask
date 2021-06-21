from flask import request
from views.shippingController import add_shipping_address, get_shipping_address
from flask_restful import Resource


class ShippingAddressHandler(Resource):
    #post address by number
    def post(self):
        request_data = request.get_json(force=True)
        resp = add_shipping_address(request_data)
        return resp
      
      #get address by number
    def get(self):
        request_data = request.args
        resp = get_shipping_address(request_data)
        return resp
        