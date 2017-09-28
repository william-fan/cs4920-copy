import services.UserProfileService

"""Can contain any number of status strings, the only requirement is that the string representing availability is in index 0."""
statuses = ["Available","In-Class","Off-Campus"]

def valid_username(username):
    return True

def change_username(user, newusername):
    existing = services.UserProfileService.find_by_username(newusername)
    if newusername != user.username and valid_username(newusername) and existing is None:
        user.username = newusername

def change_password(user, newpassword):
    if newpassword != user.password:
        user.password = newpassword
    
def change_email(user, newemail):
    # assumes already checked for email format by input field
    existing = services.UserProfileService.find_by_email(newemail)
    if newemail != user.email and existing is None:
        user.email = newemail

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
    if newstatus != user.status:
        user.status = newstatus
        
def change_imgpath(user, newimgpath):
    if newimgpath != user.imgpath:
        user.imgpath = newimgpath

def change_degree(user, newdegree):
    if newdegree != user.degree:
        user.degree = newdegree
