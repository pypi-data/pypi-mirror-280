from .BaseEntity import BaseEntity
from .InstrumentResponse import InstrumentResponse

class Instrument(BaseEntity):
    Token = ""
    IssuerBank = ""
    CustomerIdentifier = ""
    ResponseDetails = InstrumentResponse()
    CustomFields = dict()