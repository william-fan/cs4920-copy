#!/usr/local/bin/python3.6
import sys, datetime
sys.path.append('./')
from utilities.profile import *
from services.UserProfileService import *
from services.SQLService import *
import classes.UserProfile

def test_change_username():
    print("Testing username changing...")
    user = find_by_id(1)
    assert user.username == 'status'
    change_username(user, 'settings')
    new_user = find_by_id(1)
    assert new_user.username != 'status'
    assert new_user.username == 'settings'
    change_username(new_user, 'service')
    check = find_by_id(1)
    assert check.username != 'service'
    assert check.username == 'settings'
    change_username(check, 'status')
    last = find_by_id(1)
    assert last.username == 'status'
    print("Username changing OK!")

def test_change_password():
    print("Testing password changing...")
    user = find_by_id(1)
    assert user.password == 'dummy'
    change_password(user, 'newpass')
    new_user = find_by_id(1)
    assert new_user.password != 'dummy'
    assert new_user.password == 'newpass'
    change_password(new_user, 'dummy')
    last = find_by_id(1)
    assert last.password == 'dummy'
    print("Password changing OK!")
    
def test_change_email():
    print("Testing email changing...")
    user = find_by_id(1)
    assert user.email == 'dummy@dummy.dummy'
    change_email(user, 'new@new.new')
    new_user = find_by_id(1)
    assert new_user.email != 'dummy@dummy.dummy'
    assert new_user.email == 'new@new.new'
    change_email(new_user, 'service@service.com')
    check = find_by_id(1)
    assert check.email != 'service@service.com'
    assert check.email == 'new@new.new'
    change_email(check, 'dummy@dummy.dummy')
    last = find_by_id(1)
    assert last.email == 'dummy@dummy.dummy'
    print("Email changing OK!")

def test_change_firstname():
    print("Testing first name changing...")
    user = find_by_id(1)
    assert user.first_name == 'dummy'
    change_firstname(user, 'newfirst')
    new_user = find_by_id(1)
    assert new_user.first_name != 'dummy'
    assert new_user.first_name == 'newfirst'
    change_firstname(new_user, 'dummy')
    last = find_by_id(1)
    assert last.first_name == 'dummy'
    print("First name changing OK!")
    
def test_change_lastname():
    print("Testing last name changing...")
    user = find_by_id(1)
    assert user.last_name == 'dummy'
    change_lastname(user, 'newlast')
    new_user = find_by_id(1)
    assert new_user.last_name != 'dummy'
    assert new_user.last_name == 'newlast'
    change_lastname(new_user, 'dummy')
    last = find_by_id(1)
    assert last.last_name == 'dummy'
    print("Last name changing OK!")
    
def test_change_gender():
    print("Testing gender changing...")
    user = find_by_id(1)
    assert user.gender == 'dummy'
    change_gender(user, 'newgender')
    new_user = find_by_id(1)
    assert new_user.gender != 'dummy'
    assert new_user.gender == 'newgender'
    change_gender(new_user, 'dummy')
    last = find_by_id(1)
    assert last.gender == 'dummy'
    print("Gender changing OK!")
    
def test_change_dob():
    print("Testing date of birth changing...")
    user = find_by_id(1)
    assert user.dob == 'dummy'
    change_dob(user, 'newdob')
    new_user = find_by_id(1)
    assert new_user.dob != 'dummy'
    assert new_user.dob == 'newdob'
    change_dob(new_user, 'dummy')
    last = find_by_id(1)
    assert last.dob == 'dummy'
    print("Date of birth changing OK!")
    
def test_change_status():
    print("Testing status changing...")
    user = find_by_username('status')
    assert user.status == statuses[0]
    for status in statuses:
        change_status(user, status)
        user = find_by_username('status')
        assert user.status == status
    change_status(user, statuses[0])
    change_status(user, 'notastatus')
    check = find_by_username('status')
    assert check.status != 'notastatus'
    assert check.status == statuses[0]
    print("Status changing OK!")
    
def test_change_imgpath():
    print("Testing image path changing...")
    user = find_by_id(1)
    assert user.imgpath == 'dummy.jpg'
    change_imgpath(user, 'new.jpg')
    new_user = find_by_id(1)
    assert new_user.imgpath != 'dummy.jpg'
    assert new_user.imgpath == 'new.jpg'
    change_imgpath(new_user, 'dummy.jpg')
    last = find_by_id(1)
    assert last.imgpath == 'dummy.jpg'
    print("Image path changing OK!")

def test_change_degree():
    print("Testing degree changing...")
    user = find_by_id(1)
    assert user.degree == 'Computer Science'
    change_degree(user, 'fake degree')
    new_user = find_by_id(1)
    assert new_user.degree != 'Computer Science'
    assert new_user.degree == 'fake degree'
    change_degree(new_user, 'Computer Science')
    last = find_by_id(1)
    assert last.degree== 'Computer Science'
    print("Degree changing OK!")
    
def test_is_private():
    print("Testing privacy settings...")
    user = find_by_id(1)
    assert is_private(user, 'email')
    assert is_private(user, 'gender')
    assert is_private(user, 'dob')
    assert is_private(user, 'degree')
    user = find_by_id(2)
    assert is_private(user, 'email')
    assert not is_private(user, 'gender')
    assert not is_private(user, 'dob')
    assert is_private(user, 'degree')
    
    print("Privacy settings OK!")
    
def test_is_auto_update():
    print("Testing auto update check...")
    user = find_by_id(1)
    assert is_auto_update(user)
    user = find_by_id(2)
    assert not is_auto_update(user)
    print("Auto update check OK!")
    
def test_set_flags():
    print("Testing flag setting...")
    user = find_by_id(1)
    assert is_private(user, 'email')
    assert is_private(user, 'gender')
    assert is_private(user, 'dob')
    assert is_private(user, 'degree')
    assert is_auto_update(user)
    set_flags(user)
    user = find_by_id(1)
    assert is_private(user, 'email')
    assert is_private(user, 'gender')
    assert is_private(user, 'dob')
    assert is_private(user, 'degree')
    assert is_auto_update(user)
    set_flags(user, gender = False)
    user = find_by_id(1)
    assert is_private(user, 'email')
    assert not is_private(user, 'gender')
    assert is_private(user, 'dob')
    assert is_private(user, 'degree')
    assert is_auto_update(user)
    set_flags(user, dob = False)
    user = find_by_id(1)
    assert is_private(user, 'email')
    assert not is_private(user, 'gender')
    assert not is_private(user, 'dob')
    assert is_private(user, 'degree')
    assert is_auto_update(user)
    set_flags(user, email = False, dob = True)
    user = find_by_id(1)
    assert not is_private(user, 'email')
    assert not is_private(user, 'gender')
    assert is_private(user, 'dob')
    assert is_private(user, 'degree')
    assert is_auto_update(user)
    set_flags(user, email = True, gender = True, degree = False)
    user = find_by_id(1)
    assert is_private(user, 'email')
    assert is_private(user, 'gender')
    assert is_private(user, 'dob')
    assert not is_private(user, 'degree')
    assert is_auto_update(user)
    set_flags(user, degree = True, auto = False)
    assert is_private(user, 'email')
    assert is_private(user, 'gender')
    assert is_private(user, 'dob')
    assert is_private(user, 'degree')
    assert not is_auto_update(user)
    set_flags(user, email = True, gender = True, dob = True, degree = True, auto = True)
    user = find_by_id(1)
    assert is_private(user, 'email')
    assert is_private(user, 'gender')
    assert is_private(user, 'dob')
    assert is_private(user, 'degree')
    assert is_auto_update(user)
    print("Flag setting OK!")
    
def test_auto_update_status():
    print("Testing automatic status change...")
    profiles = sorted([load_profile(row) for row in execute_sql("SELECT * FROM user_profile")], key=lambda item : item.user_id)
    assert profiles[0].last_update == -1
    assert profiles[1].last_update == -1
    set_flags(profiles[1], auto=True)
    assert is_auto_update(profiles[0])
    assert is_auto_update(profiles[1])
    now = datetime.datetime(2017, 10, 9, hour=9)
    profiles = update_statuses(profiles, current=now)
    assert profiles[0].status == statuses[1]
    assert profiles[1].status == statuses[2]
    assert profiles[0].last_update == 9
    assert profiles[1].last_update == 9
    now += datetime.timedelta(hours=1) # 10
    profiles = update_statuses(profiles, current=now)
    assert profiles[0].status == statuses[1]
    assert profiles[1].status == statuses[1]
    assert profiles[0].last_update == 10
    assert profiles[1].last_update == 10
    now += datetime.timedelta(hours=4) # 14
    profiles = update_statuses(profiles, current=now)
    assert profiles[0].status == statuses[0]
    assert profiles[1].status == statuses[1]
    assert profiles[0].last_update == 14
    assert profiles[1].last_update == 14
    now += datetime.timedelta(hours=1) # 15
    profiles = update_statuses(profiles, current=now)
    assert profiles[0].status == statuses[1]
    assert profiles[1].status == statuses[0]
    assert profiles[0].last_update == 15
    assert profiles[1].last_update == 15
    set_flags(profiles[1], auto=False)
    now += datetime.timedelta(hours=2) # 17
    profiles = update_statuses(profiles, current=now)
    assert profiles[0].status == statuses[1]
    assert profiles[1].status == statuses[0]
    assert profiles[0].last_update == 17
    assert profiles[1].last_update == 15
    set_flags(profiles[1], auto=True)
    now += datetime.timedelta(hours=5) # 22
    profiles = update_statuses(profiles, current=now)
    assert profiles[0].status == statuses[2]
    assert profiles[1].status == statuses[2]
    assert profiles[0].last_update == 22
    assert profiles[1].last_update == 22
    set_flags(profiles[1], auto=False)
    for user in profiles:
        user = change_status(user, statuses[0])
        assert user.status == statuses[0]
        user.last_update = -1
        assert user.last_update == -1
    print("Automatic status changing OK!")

print("==Testing user profile settings...==")
try:
    test_change_username()
    test_change_password()
    test_change_email()
    test_change_firstname()
    test_change_lastname()
    test_change_gender()
    test_change_dob()
    test_change_status()
    test_change_imgpath()
    test_change_degree()
    test_is_private()
    test_is_auto_update()
    test_set_flags()
    test_auto_update_status()
except:
    update_user(1, username='status', password='dummy', firstname='dummy', lastname='dummy', email='dummy@dummy.dummy', gender='dummy', dob='dummy', status='Available', imgpath='dummy.jpg', degree='Computer Science', flags=-1, last_update=-1)
    update_user(2, status='Available', flags=9, last_update=-1)
    assert False

print("==User profile settings OK!==")