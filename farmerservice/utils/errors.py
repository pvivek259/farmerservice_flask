from flask import jsonify


class ErrorHandler(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_resp(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return (rv, self.status_code)



class PhoneNoDoesNotExitsError(ErrorHandler):
    pass 

class SchemaValidationError(ErrorHandler):
    pass 
