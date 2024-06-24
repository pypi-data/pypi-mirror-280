from .ValidationError import *

class CustomerEntityResponse(object):
     ValidationErrors = ValidationError()
     IsSuccess = False
     ResponseSummary = ""
     ResponseCode = ""
     Id = ""

     @property
     def AccountToken(self):
         return self.Id
        


