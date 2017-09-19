class ToDo:

    def __init__(self, name, create_time, end_time, subject, text):
        self._name = name
        self._create_time = create_time
        self._end_time = end_time
        self._subject = subject
        self._text = text

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def create_time(self):
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        self._create_time = create_time

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        self._end_time = end_time

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def status(self, subject):
        self._subject = subject

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self, text):
        self._text = text

