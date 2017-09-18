class UserProfile:

    def __init__(self, id, username, password, firstName, lastName, email, gender, dob, status, imgpath):
        self.id = id
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.gender = gender
        self.dob = dob
        self.status = status
        self.imgpath = imgpath

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName):
        self.__firstName = firstName

    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName):
        self.__lastName = lastName

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def dob(self):
        return self.__dob

    @dob.setter
    def dob(self, dob):
        self.__dob = dob

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def imgpath(self):
        return self.__imgpath

    @imgpath.setter
    def imgpath(self, imgpath):
        self.__imgpath = imgpath





