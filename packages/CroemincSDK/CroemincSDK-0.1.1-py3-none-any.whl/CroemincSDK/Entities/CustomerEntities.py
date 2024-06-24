from .Beneficiary import *
from .CustomerEntityResponse import *
from .BaseEntity import * 

class CustomerEntities(BaseEntity):
    Id = 0
    AccountNumber = ""
    ServiceType = ""
    ServiceTypeName = ""
    CustomFields = dict()
    PrimaryReferenceEntityValue = ""
    EntityBeneficiary = Beneficiary()
    ResponseDetails = CustomerEntityResponse()

    @property
    def AccountToken(self):
        return str(self.Id)



