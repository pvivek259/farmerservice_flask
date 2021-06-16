from farmerservice.views.shippingController import add_shipping_address, get_shipping_address
from flask_restful import Resource
class ShippingAddressHandler(Resource):
    def post(self):
        request_data = self.post
        resp = add_shipping_address(request)
        return resp

    def get(self):
        request_data = self.get
        resp = get_shipping_address(request)
        return resp