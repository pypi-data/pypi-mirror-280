from CroemincSDK.Entities import *
from CroemincSDK import *

class TranslationHelper(object):

    @staticmethod
    def ToCustomerResponse(decRes):
        cust = Customer()
        cust.CustomerId = decRes['CustomerId']
        cust.FirstName = decRes['FirstName']
        cust.LastName = decRes['LastName']
        cust.UniqueIdentifier = decRes['UniqueIdentifier']
        cust.Email = decRes['Email']
        cust.Fax = decRes['Fax']     
        cust.Phone = decRes['Phone']
        cust.Website = decRes['Website']
        cust.Company = decRes['Company']

        if decRes['CustomFields'] is not None:
            for item in decRes['CustomFields']:
                cust.CustomFields[item] = decRes['CustomFields'][item]

        cust.ResponseDetails = CustomerResponse()
        
        if decRes['ResponseDetails'] is not None:
                cust.ResponseDetails.CustomerId = decRes['ResponseDetails']['CustomerId']
                cust.ResponseDetails.IsSuccess = decRes['ResponseDetails']['IsSuccess']
                cust.ResponseDetails.ResponseCode = decRes['ResponseDetails']['ResponseCode']
                cust.ResponseDetails.ResponseSummary = decRes['ResponseDetails']['ResponseSummary']    
                cust.ResponseDetails.ValidationErrors = TranslationHelper.ToValidationResponse(decRes['ResponseDetails']['ValidationErrors'])
        if decRes['CreditCards'] is not None:
            cust.CreditCards = list()
            for ccItem in decRes['CreditCards']:
                cc = TranslationHelper.ToCreditCardResponse(ccItem)
                cust.CreditCards.append(cc)

        if decRes['ACHs'] is not None:
            cust.ACHs = list()
            for achItem in decRes['ACHs']:
                ach = TranslationHelper.ToACHResponse(achItem)
                cust.ACHs.append(ach)

        if decRes['CustomerEntities'] is not None:
            cust.CustomerEntities = list()
            for entityItem in decRes['CustomerEntities']:
                entity = TranslationHelper.ToCustomerEntityResponse(entityItem)
                cust.CustomerEntities.append(entity)

        if decRes['Wallet'] is not None:
            cust.Wallet.WalletNumber = decRes['Wallet']['WalletNumber']
            cust.Wallet.WalletHolder = decRes['Wallet']['WalletHolder']
            cust.Wallet.WalletBalance = decRes['Wallet']['WalletBalance']
            cust.Wallet.Token = decRes['Wallet']['Token']
            cust.Wallet.CustomerIdentifier = decRes['Wallet']['CustomerIdentifier']

            if decRes['Wallet']['CustomFields'] is not None:
                for item in decRes['Wallet']['CustomFields']:
                    cust.Wallet.CustomFields[item] = decRes['Wallet']['CustomFields'][item]

            if decRes['Wallet']['ResponseDetails'] is not None:
                cust.Wallet.ResponseDetails.Id = decRes['Wallet']['ResponseDetails']['Id']
                cust.Wallet.ResponseDetails.IsSuccess = decRes['Wallet']['ResponseDetails']['IsSuccess']
                cust.Wallet.ResponseDetails.ResponseCode = decRes['Wallet']['ResponseDetails']['ResponseCode']
                cust.Wallet.ResponseDetails.ResponseSummary = decRes['Wallet']['ResponseDetails']['ResponseSummary']
                cust.Wallet.ResponseDetails.ValidationErrors = TranslationHelper.ToValidationResponse(decRes['Wallet']['ResponseDetails']['ValidationErrors'])    
                  
        if decRes['PaymentInstructions'] is not None:
            cust.PaymentInstructions = list()
            for piItem in decRes['PaymentInstructions']:
                pi = TranslationHelper.ToPaymentInstructionResponse(piItem)
                cust.PaymentInstructions.append(pi)

        if decRes['BillingAddress'] is not None:
            cust.BillingAddress = list()
            for addressItem in decRes['BillingAddress']:
                billing = TranslationHelper.ToAddressResponse(addressItem)
                cust.BillingAddress.append(billing)

        if decRes['ShippingAddress'] is not None:
            cust.ShippingAddress = list()
            for addressItem in decRes['ShippingAddress']:
                shipping = TranslationHelper.ToAddressResponse(addressItem)
                cust.ShippingAddress.append(shipping)               

        return cust;

    @staticmethod
    def ToValidationResponse(decRes):
        ve = ValidationError()
        if decRes is not None:      
            ve.Count = decRes['Count']
            ve.ErrorDescription = decRes['ErrorDescription']
            ve.ErrorSummary = decRes['ErrorSummary']
            ve.ErrorDetails = []
            if decRes['ErrorDetails'] is not None:
                for valError in decRes['ErrorDetails']:
                    error = TranslationHelper.ToValidationResponse(valError)
                    ve.ErrorDetails.append(error)
        return ve

    @staticmethod
    def ToCreditCardResponse(decRes):
        cc = CreditCard()
        cc.CardholderName = decRes['CardholderName']
        cc.Number = decRes['Number']
        cc.ExpirationDate = decRes['ExpirationDate']
        cc.Token = decRes['Token']
        cc.CustomerId = decRes['CustomerId']
        cc.FriendlyName = decRes['FriendlyName']
        cc.Status = decRes['Status']        
        cc.CardType = decRes['CardType']
        cc.ResponseDetails = InstrumentResponse()

        if decRes['CustomFields'] is not None:
            for item in decRes['CustomFields']:
                cc.CustomFields[item] = decRes['CustomFields'][item]

        if decRes['ResponseDetails'] is not None:
                cc.ResponseDetails.Id = decRes['ResponseDetails']['Id']
                cc.ResponseDetails.IsSuccess = decRes['ResponseDetails']['IsSuccess']
                cc.ResponseDetails.ResponseCode = decRes['ResponseDetails']['ResponseCode']
                cc.ResponseDetails.ResponseSummary = decRes['ResponseDetails']['ResponseSummary']
                cc.ResponseDetails.ValidationErrors = TranslationHelper.ToValidationResponse(decRes['ResponseDetails']['ValidationErrors'])      

        return cc

    @staticmethod
    def ToACHResponse(decRes):
        ach = ACH()
        ach.AccountNumber = decRes['AccountNumber']
        ach.AccountHolder = decRes['AccountHolder']
        ach.ChequeNumber = decRes['ChequeNumber']
        ach.Token = decRes['Token']
        ach.IssuerBank = decRes['IssuerBank']
        ach.CustomerId = decRes['CustomerId']
        ach.FriendlyName = decRes['FriendlyName']
        ach.Status = decRes['Status']
        ach.CustomerIdentifier = decRes['CustomerIdentifier']
        ach.ResponseDetails = InstrumentResponse()

        if decRes['CustomFields'] is not None:
            for item in decRes['CustomFields']:
                ach.CustomFields[item] = decRes['CustomFields'][item]

        if decRes['ResponseDetails'] is not None:
                ach.ResponseDetails.Id = decRes['ResponseDetails']['Id']
                ach.ResponseDetails.IsSuccess = decRes['ResponseDetails']['IsSuccess']
                ach.ResponseDetails.ResponseCode = decRes['ResponseDetails']['ResponseCode']
                ach.ResponseDetails.ResponseSummary = decRes['ResponseDetails']['ResponseSummary']
                ach.ResponseDetails.ValidationErrors = TranslationHelper.ToValidationResponse(decRes['ResponseDetails']['ValidationErrors'])      
        return ach

    @staticmethod
    def ToPaymentInstructionResponse(decRes):
        pi = PaymentInstruction()
        pi.Id = decRes['Id']
        pi.CustomerId = decRes['CustomerId']
        pi.CustomerEntityId = decRes['CustomerEntityId']
        pi.InstrumentToken = decRes['InstrumentToken']
        pi.Status = decRes['Status']
        pi.ScheduleDay = decRes['ScheduleDay']
        pi.ExpirationDate = decRes['ExpirationDate']
        pi.CustomerEntityValue = decRes['CustomerEntityValue']
        pi.Response = PaymentInstructionResponse()

        if decRes['Response'] is not None:
                pi.Response.Id = decRes['Response']['Id']
                pi.Response.IsSuccess = decRes['Response']['IsSuccess']
                pi.Response.ResponseCode = decRes['Response']['ResponseCode']
                pi.Response.ResponseSummary = decRes['Response']['ResponseSummary']
                pi.Response.ValidationErrors = TranslationHelper.ToValidationResponse(decRes['Response']['ValidationErrors'])      

        return pi

    @staticmethod
    def ToServiceResponse(decRes):
        service = Service()
        service.Id = decRes['Id']
        service.Name = decRes['Name']
        service.Description = decRes['Description']
        service.IdentificationName = decRes['IdentificationName']            
             
        if decRes['CustomFields'] is not None:
            for item in decRes['CustomFields']:
                service.CustomFields[item] = decRes['CustomFields'][item]

        return service

    @staticmethod
    def ToCustomerEntityResponse(decRes):
        ent = CustomerEntities()
        ent.Id = decRes['Id']
        ent.AccountNumber = decRes['AccountNumber']
        ent.ServiceType = decRes['ServiceType']
        ent.ServiceTypeName = decRes['ServiceTypeName']
        ent.PrimaryReferenceEntityValue = decRes['PrimaryReferenceEntityValue']
        ent.CustomerId = decRes['CustomerId']
        ent.FriendlyName = decRes['FriendlyName']
        ent.Status = decRes['Status']
        ent.ResponseDetails = CustomerEntityResponse()
        ent.EntityBeneficiary = Beneficiary()

        if decRes['CustomFields'] is not None:
            for item in decRes['CustomFields']:
                ent.CustomFields[item] = decRes['CustomFields'][item]

        if decRes['EntityBeneficiary'] is not None:
                ent.EntityBeneficiary.Id = decRes['EntityBeneficiary']['Id']
                ent.EntityBeneficiary.Name = decRes['EntityBeneficiary']['Name']
                ent.EntityBeneficiary.ShortCode = decRes['EntityBeneficiary']['ShortCode']
                ent.EntityBeneficiary.MerchantId = decRes['EntityBeneficiary']['MerchantId']
                ent.EntityBeneficiary.Type = decRes['EntityBeneficiary']['Type']
                ent.EntityBeneficiary.Status = decRes['EntityBeneficiary']['Status']
                if decRes['EntityBeneficiary']['Services'] is not None:
                    for serviceItem in decRes['EntityBeneficiary']['Services']:
                        service = TranslationHelper.ToServiceResponse(serviceItem)
                        ent.EntityBeneficiary.Services.append(service)

        if decRes['ResponseDetails'] is not None:
                ent.ResponseDetails.Id = decRes['ResponseDetails']['Id']
                ent.ResponseDetails.IsSuccess = decRes['ResponseDetails']['IsSuccess']
                ent.ResponseDetails.ResponseCode = decRes['ResponseDetails']['ResponseCode']
                ent.ResponseDetails.ResponseSummary = decRes['ResponseDetails']['ResponseSummary']
                ent.ResponseDetails.ValidationErrors = TranslationHelper.ToValidationResponse(decRes['ResponseDetails']['ValidationErrors'])   
        return ent

    @staticmethod
    def ToAddressResponse(decRes):
        adr = Address()
        adr.AddressId = decRes['AddressId']
        adr.AddressLine1 = decRes['AddressLine1']
        adr.AddressLine2 = decRes['AddressLine2']
        adr.City = decRes['City']
        adr.CountryName = decRes['CountryName']
        adr.SubDivision = decRes['SubDivision']
        adr.State = decRes['State']
        adr.ZipCode = decRes['ZipCode']
        return adr

    @staticmethod
    def ToCustomerErrorResponse(msg):
        cust = Customer()
        cust.ResponseDetails.IsSuccess = False
        cust.ResponseDetails.ResponseCode = msg
        return cust

    @staticmethod
    def ToTransactionResponse(decRes):
        transRequest = Transaction()
        transRequest.ResponseDetails = TransactionResponse()
        
        transRequest.TerminalId = decRes["TerminalId"]
        transRequest.Amount = decRes["Amount"]
        transRequest.OrderTrackingNumber = decRes["OrderTrackingNumber"]
        transRequest.OrderId = decRes["OrderId"]
        transRequest.TransactionId = decRes["TransactionId"]
        transRequest.ThirdPartyStatus = decRes["ThirdPartyStatus"]
        transRequest.ThirdPartyDescription = decRes["ThirdPartyDescription"]
                
        if  decRes['CreditCardDetail'] is not None:
            transRequest.CreditCardDetail = TranslationHelper.ToCreditCardResponse(decRes['CreditCardDetail'])

        if  decRes['BillingAddress'] is not None:
            transRequest.BillingAddress = TranslationHelper.ToAddressResponse(decRes['BillingAddress'])

        if  decRes['ShippingAddress'] is not None:
            transRequest.ShippingAddress = TranslationHelper.ToAddressResponse(decRes['ShippingAddress'])

        if decRes['CustomFields'] is not None:
            for item in decRes['CustomFields']:
                transRequest.CustomFields[item] = decRes['CustomFields'][item]

        if  decRes['CustomerData'] is not None:
            transRequest.CustomerData = TranslationHelper.ToCustomerResponse(decRes['CustomerData'])

        if  decRes['CustomerEntityDetail'] is not None:
            transRequest.CustomerEntityDetail = TranslationHelper.ToCustomerEntityResponse(decRes['CustomerEntityDetail'])

        if  decRes['ResponseDetails'] is not None:
            transRequest.ResponseDetails.TransactionId = decRes['ResponseDetails']['TransactionId']
            transRequest.ResponseDetails.AuthorizationNumber = decRes['ResponseDetails']['AuthorizationNumber']
            transRequest.ResponseDetails.IsSuccess = decRes['ResponseDetails']['IsSuccess']
            transRequest.ResponseDetails.ResponseCode = decRes['ResponseDetails']['ResponseCode']
            transRequest.ResponseDetails.ResponseSummary = decRes['ResponseDetails']['ResponseSummary']
            transRequest.ResponseDetails.ValidationErrors = TranslationHelper.ToValidationResponse(decRes['ResponseDetails']['ValidationErrors'])

        return transRequest

