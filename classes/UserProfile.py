class UserProfile:

    def __init__(self, id, userType, username, password, firstName, lastName, email, gender, dob, status, imgpath):
        self.id = id
        self.userType = userType
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
        return self.id

    @id.setter
    def id(self, id):
        self.id = id

    @property
    def userType(self):
        return self.userType

    @userType.setter
    def userType(self, userType):
        self.userType = userType

    @property
    def username(self):
        return self.username

    @username.setter
    def username(self, username):
        self.username = username

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.password = password

    @property
    def firstName(self):
        return self.firstName

    @firstName.setter
    def firstName(self, firstName):
        self.firstName = firstName

    @property
    def lastName(self):
        return self.lastName

    @lastName.setter
    def lastName(self, lastName):
        self.lastName = lastName

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def gender(self):
        return self.gender

    @gender.setter
    def gender(self, gender):
        self.gender = gender

    @property
    def dob(self):
        return self.dob

    @dob.setter
    def dob(self, dob):
        self.dob = dob

    @property
    def status(self):
        return self.status

    @status.setter
    def status(self, status):
        self.status = status

    @property
    def imgpath(self):
        return self.imgpath

    @imgpath.setter
    def imgpath(self, imgpath):
        self.imgpath = imgpath





