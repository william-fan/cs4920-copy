class UserClass:

    def __init__(self, id, userId, courseName, startTime, endTime):
        self.id = id
        self.userId = userId
        self.courseName = courseName
        self.startTime = startTime
        self.endTime = endTime

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self, userId):
        self.__userId = userId

    @property
    def courseName(self):
        return self.__courseName

    @courseName.setter
    def courseName(self, courseName):
        self.__courseName = courseName

    @property
    def startTime(self):
        return self.__startTime

    @startTime.setter
    def startTime(self, startTime):
        self.__startTime = startTime

    @property
    def endTime(self):
        return self.__endTime

    @endTime.setter
    def endTime(self, endTime):
        self.__endTime = endTime


