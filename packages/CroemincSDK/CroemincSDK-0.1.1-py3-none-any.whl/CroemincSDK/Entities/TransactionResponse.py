from .ValidationError import ValidationError

class TransactionResponse(object):
    ValidationErrors = ValidationError()
    IsSuccess = False
    ResponseSummary = ""
    AuthorizationNumber = ""
    ResponseCode = ""
    TransactionId = ""