from .ValidationError import ValidationError

class InstrumentResponse(object):
    Id = ""
    IsSuccess = False
    ResponseSummary = ""
    ResponseCode = ""
    ValidationErrors = ValidationError()

    @property
    def InstrumentToken(self):
        return self.Id

    @property
    def CardToken(self):
        return self.Id



