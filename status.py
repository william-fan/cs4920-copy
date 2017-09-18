from enum import Enum
class Status(Enum):
    AVAILABLE = "Available"
    INCLASS = "In-Class"
    OFFCAMPUS = "Off-Campus"

def change_status(user, newstatus):
    user.status = newstatus