from .PaymentInstructionResponse import *

class PaymentInstruction(object):
    Id = ""
    CustomerId = ""
    CustomerEntityId = ""
    InstrumentToken = ""
    Status = ""
    ScheduleDay = ""
    ExpirationDate = ""
    CustomFields = dict()
    Response = PaymentInstructionResponse()
    CustomerEntityValue = ""

    @property
    def AccountToken(self):
        return self.CustomerEntityId

    @property
    def AccountNumber(self):
        return self.CustomerEntityValue


