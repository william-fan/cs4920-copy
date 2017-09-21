"""Can contain any number of status strings, the only requirement is that the string representing availability is in index 0."""
statuses = ["Available","In-Class","Off-Campus"]

def change_status(user, newstatus):
    if newstatus != user.status:
        user.status = newstatus
