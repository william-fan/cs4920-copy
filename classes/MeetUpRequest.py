class MeetUpRequest:

    def __init__(self, from_id, to_id, status, description, date):
        self._from_id = from_id
        self._to_id = to_id
        self._status = status
        self._description = description
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
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date
