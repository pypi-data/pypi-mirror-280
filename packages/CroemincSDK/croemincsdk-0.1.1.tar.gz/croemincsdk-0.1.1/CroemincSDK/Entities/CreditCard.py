from .Instrument import Instrument
from .Address import Address

class CreditCard(Instrument):
    CardholderName = ""
    Number = ""
    CVV = ""
    ExpirationDate = ""
    ExpirationMonth = ""
    ExpirationYear = ""
    CardType = ""
    IsVerified = False
    CreatedDate = ""
    CustomFields = dict()
    Address = Address()