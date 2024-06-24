class CroemincSDK:
    def __init__(self, environment, merchantId, terminalId, publicKey, privateKey, culture = "es"):
        self.__Environment = environment
        self._MerchantId = merchantId
        self._TerminalId = terminalId
        self._PublicKey = publicKey
        self._PrivateKey = privateKey
        self.SDKVersion = "1.3"
        self._Culture = culture        

        if self.__Environment == "SANDBOX":
            self._GatewayURL = "http://securegateway.merchantprocess.net/NeoGatewayAPI_Test/api/"
        elif self.__Environment == "PRODUCTION":
            self._GatewayURL = "https://gateway.merchantprocess.net/api/prod-v1.0/api/"
        else:
            raise Exception("Invalid Enviroment")