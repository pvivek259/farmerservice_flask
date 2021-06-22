from utils.errors import PhoneNoDoesNotExitsError
from flask import jsonify
import jsonschema
from dao.schemas import create_farmer_schema
from farmer.models import Farmer, PrimaryAddress
from django.core.exceptions import ObjectDoesNotExist


def create_farmer(request_param):

    # Validate this request param from the schema, if not validated return with error
    try:
        jsonschema.validate(request_param, create_farmer_schema)
    except jsonschema.exceptions.ValidationError as error:
        print(error)
        error_response={"message":':'.join(error.relative_schema_path) +":-" + error.message}
        return jsonify(error_response)

    phone_num = request_param.get("phone_no", None)
    if phone_num == None:
        error_response={"message":"please give phone Number."}
        return jsonify(error_response)

        

    #add other details and save
    farmer_object, ok =  Farmer.objects.get_or_create(phone_no = phone_num)
    farmer_object.name = request_param.get("name")
    farmer_object.email = request_param.get("email")
    #farmer_object.primary_address = request_param.get("primary_address")
    farmer_object.save()


    #Create primary address

    primary_address_param = request_param.get("primary_address")
    
    # if farmner object allready have primary address get it else create it
  
    
    
    primary_address_object = PrimaryAddress.objects.create(
        name = primary_address_param.get("name"),
        pin_code = primary_address_param.get("pin_code")
    )


    primary_address_object.address1 = primary_address_param.get("address1")
    primary_address_object.address2 = primary_address_param.get("address2")
    primary_address_object.village = primary_address_param.get("village")
    primary_address_object.city = primary_address_param.get("city")
    primary_address_object.country = primary_address_param.get("country")

    primary_address_object.save()

    farmer_object.primary_address = primary_address_object
    farmer_object.save()
    
    output={"success":True,
                "message":"Farmer added with primary address."}

    return jsonify(output)


def farmer_list(request_data):
    all_farmer_objs = Farmer.objects.all()
    result = []
    for farmer_obj in all_farmer_objs:
        output={"id":farmer_obj.id, 
        "name": farmer_obj.name,
        "email": farmer_obj.email,
        "phone_no": farmer_obj.phone_no,
        "primary_address": parse_primary_address(farmer_obj.primary_address)
        }
        result.append(output)

    new_format_result_json ={"data":result}
    return jsonify(new_format_result_json)

def parse_primary_address(primary_address):
    primary_address_json = {}

    if primary_address==None:
        return primary_address_json
        
    primary_address_json["id"] = primary_address.id
    primary_address_json["name"] = primary_address.name
    primary_address_json["address1"] = primary_address.address1
    primary_address_json["address2"] = primary_address.address2
    primary_address_json["pin_code"] = primary_address.pin_code
    primary_address_json["village"] = primary_address.village
    primary_address_json["city"] = primary_address.city
    primary_address_json["country"] = primary_address.country
    return primary_address_json


#Able to get farmer by phone number.

def get_farmer(request_param):
    phone_number = request_param.get("phone_no")
    try:
        farmer_objects = Farmer.objects.get(phone_no = phone_number)
       
    except ObjectDoesNotExist:
        raise  PhoneNoDoesNotExitsError(" Given phone_no does not exists",400)

    farmer_objs= farmer_objects.name
    result_json ={"Farmer":farmer_objs}
    return jsonify(result_json)

