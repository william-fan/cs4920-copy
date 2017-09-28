class FriendRequest:

    def __init__(self, from_id, to_id, status, message, date):
        self._from_id = from_id
        self._to_id = to_id
        self._status = status
        self._message = message
        self._date = date

    @property
    def from_id(self):
        return self._from_id

    @from_id.setter
    def from_id(self, from_id):
        self._from_id = from_id

    @property
    def to_id(self):
        return self._to_id

    @to_id.setter
    def to_id(self, to_id):
        self._to_id = to_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date
