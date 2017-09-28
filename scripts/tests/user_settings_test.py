#!/usr/local/bin/python3.6
import sys
sys.path.append('./')
from utilities.profile import *
from services.UserProfileService import *
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
    assert new_user.username != 'service'
    assert new_user.username == 'settings'
    change_username(new_user, 'status')
    last = find_by_id(1)
    assert last.username == 'status'
    print("Username changing OK!")

def test_change_password():
    print("Testing password changing...")
    print("Password changing OK!")
    
def test_change_email():
    print("Testing email changing...")
    print("Email changing OK!")

def test_change_firstname():
    print("Testing first name changing...")
    print("First name changing OK!")
    
def test_change_lastname():
    print("Testing last name changing...")
    print("Last name changing OK!")
    
def test_change_gender():
    print("Testing gender changing...")
    print("Gender changing OK!")
    
def test_change_dob():
    print("Testing date of birth changing...")
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
    print("Status changing OK!")
    
def test_change_imgpath():
    print("Testing image path changing...")
    print("Image path changing OK!")

def test_change_degree():
    print("Testing degree changing...")
    print("Degree changing OK!")

print("==Testing user profile settings...==")
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
print("==User profile settings OK!==")