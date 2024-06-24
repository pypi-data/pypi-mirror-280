#import urllib3
from datetime import datetime

class AmountRangeFilter:
    Amount1 = 0
    Amount2 = 0
    Operation = ""

    def __ClearFilter(self):
        self.Amount1 = 0
        self.Amount2 = 0
        self.Operation = ""

    def GreaterThan(self, amount):
        self.__ClearFilter()
        self.Amount1 = amount
        self.Operation = "GREATER_THAN"        

    def LessThan(self, amount):
        self.__ClearFilter()
        self.Amount1 = amount
        self.Operation = "LESS_THAN"        

    def EqualTo(self, amount):
        self.__ClearFilter()
        self.Amount1 = amount
        self.Operation = "EQUAL_TO"        
        
    def Between(self, amountFrom, amountTo):
        self.__ClearFilter()
        self.Amount1 = amountFrom
        self.Amount2 = amountTo
        self.Operation = "BETWEEN"      


class DateRangeFilter:
    Date1 = None
    Date2 = None
    Operation = ""

    def __ClearFilter(self):
        self.Date1 = None
        self.Date2 = None
        self.Operation = ""

    def GreaterThan(self, date):
        self.__ClearFilter()
        self.Date1 = date
        self.Operation = "GREATER_THAN"        

    def LessThan(self, date):
        self.__ClearFilter()
        self.Date1 = date
        self.Operation = "LESS_THAN"        

    def EqualTo(self, date):
        self.__ClearFilter()
        self.Date1 = date
        self.Operation = "EQUAL_TO"        
        
    def Between(self, dateFrom, dateTo):
        self.__ClearFilter()
        self.Date1 = dateFrom
        self.Date2 = dateTo
        self.Operation = "BETWEEN"      


class TextFilter(object):
    Text = ""
    Operation = ""

    def __ClearFilter(self):
        self.Text = ""
        self.Operation = ""

    def StartsWith(self, text):
        self.__ClearFilter()
        self.Text = text
        self.Operation = "STARTS_WITH"        

    def EndsWith(self, text):
        self.__ClearFilter()
        self.Text = text
        self.Operation = "ENDS_WITH"        

    def Is(self, text):
        self.__ClearFilter()
        self.Text = text
        self.Operation = "IS"