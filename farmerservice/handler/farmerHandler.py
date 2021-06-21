from views.farmerController import create_farmer, farmer_list, get_farmer
from flask_restful import Resource
from flask import request

class FarmerHandler(Resource):
# create farmer
    def post(self):
        request_data = request.get_json(force=True)
        resp = create_farmer(request_data)
        return resp

#get farmer list
    def get(self):
        request_data = self.get
        resp = farmer_list(request_data)
        return resp

#get farmer by phone number
class GetFarmer(Resource):

    def get(self):
        request_data = request.args
        resp = get_farmer(request_data)
        return resp
