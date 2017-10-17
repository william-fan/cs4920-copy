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
        
def is_private(user, field_name):
    """Checks privacy, which uses bit flags. If the bit position is 1 then that field should be private to strangers."""
    
    EMAIL_CHECK = 0b1
    GENDER_CHECK = 0b10
    DOB_CHECK = 0b100
    DEGREE_CHECK = 0b1000
    
    if field_name == 'email':
        return user.flags & EMAIL_CHECK != 0
        
    if field_name == 'gender':
        return user.flags & GENDER_CHECK != 0
    
    if field_name == 'dob':
        return user.flags & DOB_CHECK != 0
        
    if field_name == 'degree':
        return user.flags & DEGREE_CHECK != 0

def set_flags(user, email=None, gender=None, dob=None, degree=None, auto=None):
    """Sets appropriate bit to 1 if True, 0 if False and the same as original if None"""
    newflags = 0
    if email:
        newflags |= 0b1
    elif email is None:
        newflags |= (0b1 & user.flags)
    if gender:
        newflags |= 0b10
    elif gender is None:
        newflags |= (0b10 & user.flags)
    if dob:
        newflags |= 0b100
    elif dob is None:
        newflags |= (0b100 & user.flags)
    if degree:
        newflags |= 0b1000
    elif degree is None:
        newflags |= (0b1000 & user.flags)
    if auto:
        newflags |= 0b10000
    elif auto is None:
        newflags |= (0b10000 & user.flags)

    if newflags != user.flags:
        user.flags = newflags

def is_auto_update(user):
    AUTO_CHECK = 0b10000
    return user.flags & AUTO_CHECK != 0


def update_statuses(users, current=datetime.datetime.now()):
    """Given a list of users and a datetime object, checks their timetables and updates their statuses based on the current time. Returns the updated UserProfile objects afterwards."""
    day = current.weekday()
    update_time = (day * 24) + current.hour
    # automatically off-campus if before or after standard class schedule hours or on the weekend
    if current.hour < 9 or current.hour > 21 or current.weekday() > 4:
        for i in range(0, len(users)):
            user = users[i]
            # if they do not want to be automatically updated or they have been updated for this hour already
            if not is_auto_update(user) or user.last_update == update_time:
                continue            
            users[i] = change_status(users[i], statuses[2])
            users[i].last_update = update_time
        return users
    for i in range(0, len(users)):
        user = users[i]
        if not is_auto_update(user) or user.last_update == update_time:
            continue            
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
        users[i].last_update = update_time
    return users
