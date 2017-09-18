class UserClass:

    def __init__(self, id, userId, courseName, startTime, endTime):
        self.id = id
        self.userId = userId
        self.courseName = courseName
        self.startTime = startTime
        self.endTime = endTime

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        self.id = id

    @property
    def userId(self):
        return self.userId

    @userId.setter
    def userId(self, userId):
        self.userId = userId

    @property
    def courseName(self):
        return self.courseName

    @courseName.setter
    def courseName(self, courseName):
        self.courseName = courseName

    @property
    def startTime(self):
        return self.startTime

    @startTime.setter
    def startTime(self, startTime):
        self.startTime = startTime

    @property
    def endTime(self):
        return self.endTime

    @endTime.setter
    def endTime(self, endTime):
        self.endTime = endTime


