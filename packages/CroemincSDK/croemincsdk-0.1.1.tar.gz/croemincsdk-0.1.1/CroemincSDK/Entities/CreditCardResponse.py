from .ValidationError import ValidationError

class CreditCardResponse(object):
    ValidationErrors = ValidationError()
    IsSuccess = False
    ResponseSummary = ""
    ResponseCode = ""
    Id = ""