create_farmer_schema = {
    "name": "Farmer",
    "properties": {
        "name": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "phone_no": {
            "type": "number"
        },
        "primary_address": {
            "name":"primary_address",
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "address1": {"type": "string"},
                "address2":{"type":"string"},
                "pin_code":{"type":"number"},
                "village": {"type": "string"},
                "city": {"type": "string"},
                "country": {"type": "string"},
            },
            "required":["name", "address2", ]
        }
    },
    "required" :["name", "phone_no", "email", "primary_address"]
}
