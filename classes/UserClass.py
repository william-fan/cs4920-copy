class UserClass:

    def __init__(self, user_id, course_name, start_time, end_time):
        self._user_id = user_id
        self._course_name = course_name
        self._start_time = start_time
        self._end_time = end_time
    
    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id):
        self._user_id = user_id

    @property
    def course_name(self):
        return self._course_name
        
    @course_name.setter
    def course_name(self, course_name):
        self._course_name = course_name
        
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        self._start_time = start_time
        
    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time
        
