class MeetUpRequest:

    def __init__(self, fromId, toId, status):
        self.fromId = fromId
        self.toId = toId
        self.status = status

    @property
    def fromId(self):
        return self.fromId

    @fromId.setter
    def fromId(self, fromId):
        self.fromId = fromId

    @property
    def toId(self):
        return self.toId

    @toId.setter
    def toId(self, toId):
        self.toId = toId

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        self.status = status
