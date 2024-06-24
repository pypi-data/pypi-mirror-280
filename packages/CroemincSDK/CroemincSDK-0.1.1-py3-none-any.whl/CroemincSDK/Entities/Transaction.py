from .TransactionOptions import *
from .TransactionResponse import *
from .Address import *
from .CreditCard import *
from .Customer import *
from .CustomerEntities import *
from .TransactionOptions import *
from .TransactionResponse import *

class Transaction(object):
    CreditCardDetail = CreditCard()
    PaymentMethodToken = ""
    Amount = 0
    BillingAddress = Address()
    BillingAddressId = ""
    TerminalId = ""
    OrderTrackingNumber = ""
    CustomFields = dict()
    CustomerData = Customer()
    CustomerId = ""
    TransactOptions = TransactionOptions()
    OrderId = ""
    ShippingAddress = Address()
    ShippingAddressId = ""
    ResponseDetails = TransactionResponse()
    TransactionId = ""
    CustomerEntityDetail = CustomerEntities() 
    ThirdPartyDescription = ""
    ThirdPartyStatus = ""