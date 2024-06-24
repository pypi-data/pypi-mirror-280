from .ParameterFilter import *
from .CustomerSearchOption import *
from .SearchFilter import *

class CustomerSearch(object):
    CustomerId = ""
    UniqueIdentifier = ""
    Email = TextFilter()
    Fax = TextFilter()
    FirstName = TextFilter()
    LastName = TextFilter()
    Phone = TextFilter()
    Website = TextFilter()
    Company = TextFilter()
    DateCreated = DateRangeFilter()
    InstrumentNumber = TextFilter()
    InstrumentToken = ""
    InstrumentHolderName = TextFilter()
    CustomerEntityId = ""
    CustomerEntityName = TextFilter()
    CustomerEntityNumber = TextFilter()
    SearchOption = CustomerSearchOption()
    SearchFilter = SearchFilter()