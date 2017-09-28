#!/usr/local/bin/python3.6
import sys
sys.path.append('./')
from services.UserProfileService import *
import classes.UserProfile

def test_find_by_email_pass():
    print("Testing find_by_email_pass()...")
    user = find_by_email_pass('service@service.com', 'service')
    assert user.email == 'service@service.com' and user.password == 'service'
    print("find_by_email_pass() OK!")


def test_find_by_email():
    print("Testing find_by_email()...")
    user = find_by_email('service@service.com')
    assert user.email == 'service@service.com'
    print("find_by_email() OK!")


def test_find_by_username():
    print("Testing find_by_username()...")
    user = find_by_username('service')
    assert user.username == 'service'
    print("find_by_username() OK!")


def test_find_by_id():
    print("Testing find_by_id()...")
    user = find_by_id(1)
    assert user.user_id == 1
    user = find_by_id(2)
    assert user.user_id == 2
    print("find_by_id() OK!")


def test_update_user():
    print("Testing update_user()...")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'service' and user.password == 'service' and user.first_name == 'servicefirst' and user.last_name == 'servicelast' and user.email == 'service@service.com' and user.gender == 'servicegender' and user.dob == 'servicedob' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    print("Changing each field individually...")
    update_user(user.user_id, username="newservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'service' and user.first_name == 'servicefirst' and user.last_name == 'servicelast' and user.email == 'service@service.com' and user.gender == 'servicegender' and user.dob == 'servicedob' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, password="newservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'servicefirst' and user.last_name == 'servicelast' and user.email == 'service@service.com' and user.gender == 'servicegender' and user.dob == 'servicedob' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, firstname="newservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'newservice' and user.last_name == 'servicelast' and user.email == 'service@service.com' and user.gender == 'servicegender' and user.dob == 'servicedob' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, lastname="newservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'newservice' and user.last_name == 'newservice' and user.email == 'service@service.com' and user.gender == 'servicegender' and user.dob == 'servicedob' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, email="newservice@service.com")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'newservice' and user.last_name == 'newservice' and user.email == 'newservice@service.com' and user.gender == 'servicegender' and user.dob == 'servicedob' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, gender="newservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'newservice' and user.last_name == 'newservice' and user.email == 'newservice@service.com' and user.gender == 'newservice' and user.dob == 'servicedob' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, dob="newservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'newservice' and user.last_name == 'newservice' and user.email == 'newservice@service.com' and user.gender == 'newservice' and user.dob == 'newservice' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, status="newservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'newservice' and user.last_name == 'newservice' and user.email == 'newservice@service.com' and user.gender == 'newservice' and user.dob == 'newservice' and user.status == 'newservice' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, imgpath="newservice.jpg")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'newservice' and user.last_name == 'newservice' and user.email == 'newservice@service.com' and user.gender == 'newservice' and user.dob == 'newservice' and user.status == 'newservice' and user.imgpath == 'newservice.jpg' and user.degree == 'Computer Science'
    update_user(user.user_id, degree="newservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newservice' and user.password == 'newservice' and user.first_name == 'newservice' and user.last_name == 'newservice' and user.email == 'newservice@service.com' and user.gender == 'newservice' and user.dob == 'newservice' and user.status == 'newservice' and user.imgpath == 'newservice.jpg' and user.degree == 'newservice'
    print("Changing multiple fields at a time...")
    update_user(user.user_id, username="newnewservice", password="newnewservice")
    user = find_by_id(2)
    assert user.user_id == 2 and user.username == 'newnewservice' and user.password == 'newnewservice' and user.first_name == 'newservice' and user.last_name == 'newservice' and user.email == 'newservice@service.com' and user.gender == 'newservice' and user.dob == 'newservice' and user.status == 'newservice' and user.imgpath == 'newservice.jpg' and user.degree == 'newservice'
    print("Cleaning up the changes...")
    update_user(user.user_id, username='service', password='service', firstname='servicefirst', lastname='servicelast', email='service@service.com', gender='servicegender', dob='servicedob', status='Available', imgpath='default.jpg', degree='Computer Science')
    print("Check it's all back to normal...")
    user = find_by_username('service')
    assert user.user_id == 2 and user.username == 'service' and user.password == 'service' and user.first_name == 'servicefirst' and user.last_name == 'servicelast' and user.email == 'service@service.com' and user.gender == 'servicegender' and user.dob == 'servicedob' and user.status == 'Available' and user.imgpath == 'default.jpg' and user.degree == 'Computer Science'
    print("update_user() OK!")
    

def test_get_user_id_from_username():
    print("Testing get_user_id_from_username()...")
    user_id = get_user_id_from_username('service')
    assert user_id == 2
    print("get_user_id_from_username() OK!")


def test_get_username_from_user_id():
    print("Testing get_username_from_user_id()...")
    username = get_username_from_user_id(2)
    assert username == 'service'
    print("get_username_from_user_id() OK!")


print("==Testing UserProfileService.py...==")
try:
    test_find_by_email_pass()
    test_find_by_email()
    test_find_by_username()
    test_find_by_id()
    test_update_user()
    test_get_user_id_from_username()
    test_get_username_from_user_id()
except:
    update_user(2, username='service', password='service', firstname='servicefirst', lastname='servicelast', email='service@service.com', gender='servicegender', dob='servicedob', status='Available', imgpath='default.jpg', degree='Computer Science')
    assert False
print("==UserProfileService.py OK!==")
