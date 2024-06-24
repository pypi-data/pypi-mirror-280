from .CreditCard import *
from .CustomerResponse import CustomerResponse
from .CustomerOptions import CustomerOptions
from .Address import *
from .Wallet import *

class Customer(object):
    CustomerId = ""
    UniqueIdentifier = ""
    CreditCards = list()
    CustomFields = dict()
    ACHs = list()
    CustomerEntities = list()
    PaymentInstructions = list()
    Wallet = Wallet()
    Email = ""
    Fax = ""
    FirstName = ""
    LastName = ""
    Phone = ""
    Website = ""
    Company = ""
    ResponseDetails = CustomerResponse()
    Options = CustomerOptions()
    BillingAddress = list()
    ShippingAddress = list()


