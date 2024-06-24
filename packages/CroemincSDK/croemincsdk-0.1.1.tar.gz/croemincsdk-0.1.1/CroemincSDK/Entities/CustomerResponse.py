from .ValidationError import ValidationError

class CustomerResponse(object):
    ValidationErrors = ValidationError()
    IsSuccess = False
    ResponseSummary = ""
    ResponseCode = ""
    CustomerId = ""
    UniqueIdentification = ""

    @property
    def CustomerToken(self):
        return self.CustomerId