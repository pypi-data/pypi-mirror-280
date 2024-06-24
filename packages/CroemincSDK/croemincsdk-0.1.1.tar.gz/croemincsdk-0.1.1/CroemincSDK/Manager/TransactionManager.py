import sys
sys.path.append('~\\')
sys.path.append('~\\Entities')
sys.path.append('~\\Helper')

from Entities.Transaction import *
from CroemincSDK import CroemincGateway
from Helper.TranslationHelper import *
from Entities.TransactionOptions import *
import jsonpickle,requests
from datetime import datetime

class TransactionManager(CroemincGateway):
    def __init__(self, CroemincGateway):
        self.CroemincObject = CroemincGateway

    def Sale(self, transRequest):
        transRequest.TransactOptions = TransactionOptions()
        transRequest.TransactOptions.Operation = "Sale"
        Response = self.__SendAPIRequest(transRequest, self.CroemincObject._GatewayURL + "Transaction/PerformTransaction")
        if Response is not None:
            d = jsonpickle.decode(Response.content.decode("utf-8"))
            if d["ResponseMessage"] is not None:
                decRes = jsonpickle.decode(d["ResponseMessage"])
                return TranslationHelper.ToTransactionResponse(decRes)
            else:
                return self.__ErrorResponse("ResponseMessage object is null")
        else:
            return self.__ErrorResponse("Response object is null")
        
    def PreAuthorization(self, transRequest):
        transRequest.TransactOptions = TransactionOptions()
        transRequest.TransactOptions.Operation = "PreAuthorization"
        Response = self.__SendAPIRequest(transRequest, self.CroemincObject._GatewayURL + "Transaction/PerformTransaction")
        if Response is not None:
            d = jsonpickle.decode(Response.content.decode("utf-8"))
            if d["ResponseMessage"] is not None:
                decRes = jsonpickle.decode(d["ResponseMessage"])
                return TranslationHelper.ToTransactionResponse(decRes)
            else:
                return self.__ErrorResponse("ResponseMessage object is null")
        else:
            return self.__ErrorResponse("Response object is null")
        
    def Rebill(self, transRequest):
        transRequest.TransactOptions = TransactionOptions()
        transRequest.TransactOptions.Operation = "Rebill"
        Response = self.__SendAPIRequest(transRequest, self.CroemincObject._GatewayURL + "Transaction/PerformTransaction")
        if Response is not None:
            d = jsonpickle.decode(Response.content.decode("utf-8"))
            if d["ResponseMessage"] is not None:
                decRes = jsonpickle.decode(d["ResponseMessage"])
                return TranslationHelper.ToTransactionResponse(decRes)
            else:
                return self.__ErrorResponse("ResponseMessage object is null")
        else:
            return self.__ErrorResponse("Response object is null")
        
    def Adjustment(self, transRequest):
        transRequest.TransactOptions = TransactionOptions()
        transRequest.TransactOptions.Operation = "Adjustment"
        Response = self.__SendAPIRequest(transRequest, self.CroemincObject._GatewayURL + "Transaction/PerformTransaction")
        if Response is not None:
            d = jsonpickle.decode(Response.content.decode("utf-8"))
            if d["ResponseMessage"] is not None:
                decRes = jsonpickle.decode(d["ResponseMessage"])
                return TranslationHelper.ToTransactionResponse(decRes)
            else:
                return self.__ErrorResponse("ResponseMessage object is null")
        else:
            return self.__ErrorResponse("Response object is null")

    def Refund(self, transRequest):
        transRequest.TransactOptions = TransactionOptions()
        transRequest.TransactOptions.Operation = "Refund"
        Response = self.__SendAPIRequest(transRequest, self.CroemincObject._GatewayURL + "Transaction/PerformTransaction")
        if Response is not None:
            d = jsonpickle.decode(Response.content.decode("utf-8"))
            if d["ResponseMessage"] is not None:
                decRes = jsonpickle.decode(d["ResponseMessage"])
                return TranslationHelper.ToTransactionResponse(decRes)
            else:
                return self.__ErrorResponse("ResponseMessage object is null")
        else:
            return self.__ErrorResponse("Response object is null")

    def UpdateTransactionStatus(self, transRequest):
        Response = self.__SendAPIRequest(transRequest, self.CroemincObject._GatewayURL + "Transaction/UpdateTransactionStatus")
        if Response is not None:
            d = jsonpickle.decode(Response.content.decode("utf-8"))
            if d["ResponseMessage"] is not None:
                decRes = jsonpickle.decode(d["ResponseMessage"])
                return TranslationHelper.ToTransactionResponse(decRes)
            else:
                return self.__ErrorResponse("ResponseMessage object is null")
        else:
            return self.__ErrorResponse("Response object is null")

    def SearchTransaction(self, searchFilter):
        Result = list()
        Response = self.__SendAPIRequest(searchFilter, self.CroemincObject._GatewayURL + "Transaction/SearchTransaction")
        if Response is not None:
            d = jsonpickle.decode(Response.content.decode("utf8"))
            if d["ResponseMessage"] is not None:
                transactions = jsonpickle.decode(d["ResponseMessage"])
                if transactions is not None:
                    for item in transactions:
                        Result.append(TranslationHelper.ToTransactionResponse(item))
            else:
                return Result # return empty list
        else:
            Result # return empty list

        return Result
        
    def __CreateRequestObj(self, Model):
        RequestData = {
            "Identification":self.CroemincObject._MerchantId,
            "DateTimeStamp":str(datetime.now()),
            "SDKVersion":str(self.CroemincObject.SDKVersion),
            "RequestMessage":jsonpickle.encode(Model, unpicklable=False),
            "TerminalId": self.CroemincObject._TerminalId,
            "Culture": self.CroemincObject._Culture
        }
        return RequestData
        
    def __SendAPIRequest(self, Model, RequestURL):
        HttpRequestHeaders = {'content-type': 'application/json'}
        Response = requests.post(url=RequestURL, data=jsonpickle.encode(self.__CreateRequestObj(Model), unpicklable=False), headers=HttpRequestHeaders)
        return Response

    def __ErrorResponse(self, msg):
        TransRequest = Transaction()
        TransRequest.Response = TransactionResponse()
        TransRequest.Response.IsSuccess = False
        TransRequest.Response.ResponseSummary = msg
        return TransRequest