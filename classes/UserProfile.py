class UserProfile:

    def __init__(self, user_id, user_type, username, password, first_name, last_name, email, gender, dob, status, imgpath):
        self._user_id = user_id
        self._user_type = user_type
        self._username = username
        self._password = password
        self._first__name = first_name
        self._last_name = last_name
        self._email = email
        self._gender = gender
        self._dob = dob
        self._status = status
        self._imgpath = imgpath

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def user_type(self):
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        self._user_type = user_type

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        self._gender = gender

    @property
    def dob(self):
        return self._dob

    @dob.setter
    def dob(self, dob):
        self._dob = dob

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def imgpath(self):
        return self._imgpath

    @imgpath.setter
    def imgpath(self, imgpath):
        self._imgpath = imgpath





