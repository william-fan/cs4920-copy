class PublicEvent:

    def __init__(self, id, title, description, start_time, end_time):
        self._id = id
        self._title = title
        self._description = description
        self._start_time= start_time
        self._end_time = end_time

    @property
    def id(self):
        return self._id

    @id.setter
    def name(self, id):
        self._id = id

    @property
    def title(self):
        return self._title

    @title.setter
    def name(self, title):
        self._title = title

    @property
    def description(self):
        return self._description

    @description.setter
    def name(self, description):
        self._description = description

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def name(self, start_time):
        self._start_time = start_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time


