from .ValidationError import  *

class PaymentInstructionResponse(object):
     ValidationErrors = ValidationError()
     IsSuccess = False
     ResponseSummary = ""
     ResponseCode = ""
     Id = ""

     @property
     def PaymentInstructionToken(self):
         return self.Id


