class BaseEntity(object):

    CustomerId = ""
    FriendlyName = ""
    __status = ""
   
    @property
    def Status(self):
        return self.__status

    @Status.setter
    def Status(self, value):

        if(value is not None):
            value = str(value)

        validStatus = list()
        validStatus.append("INACTIVE")
        validStatus.append("ACTIVE")
        validStatus.append("SUSPENDED")
        validStatus.append("CANCELLED")
        validStatus.append("DELETED")
        validStatus.append("VERIFIED")
        validStatus.append("BLACKLISTED")
        if value is not None and value != "0" and value != "":
            if value.upper() in validStatus:
                self.__status = value
            else:
                raise Exception('Invalid Status')