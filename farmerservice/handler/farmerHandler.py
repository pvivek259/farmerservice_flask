from farmerservice.views.farmerController import create_farmer, farmer_list, get_farmer
from flask_restful import Resource

class FarmerHandler(Resource):

    def post(self):
        request_data = self.post
        resp = create_farmer(request_param)
        return resp


    def get(self):
        request_data = self.get
        resp = farmer_list(request)
        return resp

class GetFarmer(Resource):

    def get(self):
        request_data = self.get
        resp = get_farmer(request)
        return resp
