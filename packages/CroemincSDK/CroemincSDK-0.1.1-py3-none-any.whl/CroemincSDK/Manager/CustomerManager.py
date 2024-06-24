import sys
import os

from random import *
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(src_dir)

from Entities import *
from CroemincSDK import CroemincGateway
from Entities.InstrumentResponse import InstrumentResponse
from Helper.TranslationHelper import *
import jsonpickle,requests
from datetime import datetime

class CustomerManager(CroemincGateway):
    def __init__(self, CroemincGateway):
        self.CroemincObject = CroemincGateway

    def SaveCustomer(self, customer):
        return self.__SaveEncCustomer(customer)       
        
    def SearchCustomer(self, customerfilter):
        Result = list()
        Response = self.__SendAPIRequest(customerfilter, self.CroemincObject._GatewayURL + "Customer/GetCustomersByFilter")
        if Response  is not None:
            d = jsonpickle.decode(Response.content.decode("utf-8"))
            if d["ResponseMessage"]  is not None:
                customers = jsonpickle.decode(d["ResponseMessage"])
                if customers  is not None:
                    for item in customers:
                        Result.append(TranslationHelper.ToCustomerResponse(item))
            else:
                return self.__ErrorResponse("ResponseMessage object is null")
        else:
            return self.__ErrorResponse("Response object is null")
        return Result
        
    def __SaveEncCustomer(self, customer):
        Response = self.__SendAPIRequest(customer, self.CroemincObject._GatewayURL + "Customer/SaveCustomerInformation")
        if Response  is not None:
            d = jsonpickle.decode(Response.content.decode("utf-8"))
            if d["ResponseMessage"]  is not None:
                decRes = jsonpickle.decode(d["ResponseMessage"])
                return TranslationHelper.ToCustomerResponse(decRes)
            else:
                self.__ErrorResponse("ResponseMessage object is null")
        else:
            return self.__ErrorResponse("Response object is null")
        
    def __SendAPIRequest(self, Model, RequestURL):
        HttpRequestHeaders = {'content-type': 'application/json'}
        Response = requests.post(url=RequestURL, data=jsonpickle.encode(self.__CreateRequestObj(Model), unpicklable=False), headers=HttpRequestHeaders)
        return Response
    
    def __CreateRequestObj(self, Model):
        HttpRequestHeaders = {'content-type': 'application/json'}
        RequestData = {
            "SDKVersion":self.CroemincObject.SDKVersion,
            "Identification":self.CroemincObject._MerchantId,
            "DateTimeStamp":str(datetime.now()),
            "RequestMessage":jsonpickle.encode(Model, unpicklable=False),
            "TerminalId": self.CroemincObject._TerminalId,
            "Culture": self.CroemincObject._Culture
        }
        return RequestData
        
    def __ErrorResponse(self, msg):
        cust = Customer()
        cust.ResponseDetails.IsSuccess = False
        cust.ResponseDetails.ResponseCode = msg
        return cust   