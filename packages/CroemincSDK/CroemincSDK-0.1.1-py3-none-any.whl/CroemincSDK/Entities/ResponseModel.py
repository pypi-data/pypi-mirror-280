from .ValidationError import ValidationError

class ResponseModel(object):
    APIVersion = ""
    ResponseMessage = ""
    Identification = ""
    ValidationErrors = ValidationError()



