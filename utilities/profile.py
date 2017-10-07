import datetime
import services.UserProfileService

"""Can contain any number of status strings, the only requirement is that the string representing availability is in index 0."""
statuses = ["Available","In-Class","Off-Campus"]

def valid_username(username):
    return True

def change_username(user, newusername):
    """Changes username if it is a valid username and not already taken. Returns False if username was already taken."""
    if newusername == user.username:
        return True
    existing = services.UserProfileService.find_by_username(newusername)
    if valid_username(newusername) and existing is None:
        user.username = newusername
        return True
    return False

def change_password(user, newpassword):
    if newpassword != user.password:
        user.password = newpassword
    
def change_email(user, newemail):
    """Changes email if it is not already taken. Returns False if email was already taken."""
    if newemail == user.email:
        return True
    # assumes already checked for email format by input field
    existing = services.UserProfileService.find_by_email(newemail)
    if existing is None:
        user.email = newemail
        return True
    return False

def change_firstname(user, newfirstname):
    if newfirstname != user.first_name:
        user.first_name = newfirstname
        
def change_lastname(user, newlastname):
    if newlastname != user.last_name:
        user.last_name = newlastname
        
def change_gender(user, newgender):
    if newgender != user.gender:
        user.gender = newgender
        
def change_dob(user, newdob):
    if newdob != user.dob:
        user.dob = newdob

def change_status(user, newstatus):
    if newstatus != user.status and newstatus in statuses:
        user.status = newstatus
    return user
        
def change_imgpath(user, newimgpath):
    if newimgpath != user.imgpath:
        user.imgpath = newimgpath

def change_degree(user, newdegree):
    if newdegree != user.degree:
        user.degree = newdegree

def update_statuses(users, current=datetime.datetime.now()):
    """Given a list of users and a datetime object, checks their timetables and updates their statuses based on the current time. Returns the updated UserProfile objects afterwards."""
    if current.hour < 9 or current.hour > 21 or current.weekday() > 4:
        for i in range(0, len(users)):
            users[i] = change_status(users[i], statuses[2])
        return users
    day = current.weekday()
    for i in range(0, len(users)):
        user = users[i]
        timetable = services.UserProfileService.timetable_by_id(user.user_id)
        timeslots = {i:statuses[2] for i in range(9, 22)}
        timeslot_time = 9
        class_before = False
        # filter out a list of classes on that day and sort by start time
        for user_class in sorted([_class for _class in timetable if _class['day'] == day], key=lambda item : item['time']):
            start = user_class['time']
            for j in range(timeslot_time, start):
                # if there was a class before this one then fill the time in between with available
                if class_before:
                    timeslots[j] = statuses[0]
            for j in range(start, start+user_class['length']):
                timeslots[j] = statuses[1]
            timeslot_time = start+user_class['length']
            class_before = True
        users[i] = change_status(user, timeslots[current.hour])
    return users
