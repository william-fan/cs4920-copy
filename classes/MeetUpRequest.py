class MeetUpRequest:

    def __init__(self, fromId, toId, status, description):
        self.fromId = fromId
        self.toId = toId
        self.status = status
        self.description = description

    @property
    def fromId(self):
        return self.__fromId

    @fromId.setter
    def fromId(self, fromId):
        self.__fromId = fromId

    @property
    def toId(self):
        return self.__toId

    @toId.setter
    def toId(self, toId):
        self.__toId = toId

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def description(self):
        return self.__desciption

    @status.setter
    def description(self, desciption):
        self.__desciption = desciption
