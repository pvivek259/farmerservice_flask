import django
django.setup()
from flask import jsonify
import json
from farmer.models import Farmer,ShippingAddress

def add_shipping_address(request_param):
    # Get the param
    print(request_param)
    phone_number = request_param.get("phone_no")
    print(phone_number)
    # Get farmer object
    farmer_obj = Farmer.objects.get(phone_no = phone_number)
    #create  shipping address object, and add farmer ID
    shipping_address_object = ShippingAddress.objects.create(farmer = farmer_obj)

    shipping_address_object.name = request_param.get("name", None),
    shipping_address_object.address1 = request_param.get("address1", None),
    shipping_address_object.address2 =request_param.get("address2", None),
    shipping_address_object.pin_code = request_param.get("pin_code", None),
    shipping_address_object.village = request_param.get("village", None),
    shipping_address_object.city =request_param.get("city", None),
    shipping_address_object.country =request_param.get("country", None)

    #save shipping address object
    shipping_address_object.save()
    output={"success":True,
                "message":"succesfully added the  shippingAddress."}

    return jsonify(output)



def get_shipping_address(request_param):
    phone_number= request_param.get("phone_no")
       #get the farmer object
    farmer_obj = Farmer.objects.get(phone_no = phone_number)
    #get shipping addresses object, and add farmer ID
    shipping_address_objs= farmer_obj.shippingaddress_set.all()
    
    result_json ={"data":parse_shipping_addresses(shipping_address_objs)}

    return jsonify(result_json)



def parse_shipping_addresses(shipping_address_objs):
    result = []
    for shipping_address_obj in shipping_address_objs:
        result.append(parse_shipping_address(shipping_address_obj))

    return result



def parse_shipping_address(shipping_address):
    shipping_address_json = {}
    shipping_address_json["id"] = shipping_address.id
    shipping_address_json["name"] = shipping_address.name
    shipping_address_json["address1"] = shipping_address.address1
    shipping_address_json["address2"] = shipping_address.address2
    shipping_address_json["pin_code"] = shipping_address.pin_code
    shipping_address_json["village"] = shipping_address.village
    shipping_address_json["city"] = shipping_address.city
    shipping_address_json["country"] = shipping_address.country
    return shipping_address_json
