from .ParameterFilter import *
from .SearchFilter import *

class TransactionSearch(object):
    TransactionId = ""
    OrderTrackingNumber = ""
    Token = ""
    Amount = AmountRangeFilter()
    DateCreated = DateRangeFilter()
    SettledDate = DateRangeFilter()
    CardNumber = TextFilter()
    CardHolderName = TextFilter()
    CustomerId = ""
    CustomerIdentifier = ""