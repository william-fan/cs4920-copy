class MeetUpRequest:

    def __init__(self, fromId, toId, status):
        self.fromId = fromId
        self.toId = toId
        self.status = status

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
