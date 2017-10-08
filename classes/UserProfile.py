import services.UserProfileService

class UserProfile:

    def __init__(self, user_id, username, password, first_name, last_name, email, gender, dob, status, imgpath, degree, flags, last_update):
        self._user_id = user_id
        self._username = username
        self._password = password
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._gender = gender
        self._dob = dob
        self._status = status
        self._imgpath = imgpath
        self._degree = degree
        self._flags = flags
        self._last_update = last_update

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username
        services.UserProfileService.update_user(self.user_id, username=self.username)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
        services.UserProfileService.update_user(self.user_id, password=self.password)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
        services.UserProfileService.update_user(self.user_id, firstname=self.first_name)

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
        services.UserProfileService.update_user(self.user_id, lastname=self.last_name)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
        services.UserProfileService.update_user(self.user_id, email=self.email)

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender
        services.UserProfileService.update_user(self.user_id, gender=self.gender)

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, dob):
        self._dob = dob
        services.UserProfileService.update_user(self.user_id, dob=self.dob)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
        services.UserProfileService.update_user(self.user_id, status=self.status)

    @property
    def imgpath(self):
        return self._imgpath

    @imgpath.setter
    def imgpath(self, imgpath):
        self._imgpath = imgpath
        services.UserProfileService.update_user(self.user_id, imgpath=self.imgpath)

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, degree):
        self._degree = degree
        services.UserProfileService.update_user(self.user_id, degree=self.degree)
    
    @property
    def flags(self):
        return self._flags
    
    @flags.setter
    def flags(self, flags):
        self._flags = flags
        services.UserProfileService.update_user(self.user_id, flags=self.flags)

    @property
    def last_update(self):
        return self._last_update
        
    @last_update.setter
    def last_update(self, last_update):
        self._last_update = last_update
        services.UserProfileService.update_user(self.user_id, last_update=self.last_update)
