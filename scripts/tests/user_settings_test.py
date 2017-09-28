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
except:
    update_user(1, username='status', password='dummy', firstname='dummy', lastname='dummy', email='dummy@dummy.dummy', gender='dummy', dob='dummy', status='Available', imgpath='dummy.jpg', degree='Computer Science')
    assert False
print("==User profile settings OK!==")