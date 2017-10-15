#!/usr/local/bin/python3.6
import sys
sys.path.append('./')
from services.UserProfileService import *
import services.SQLService
import classes.UserProfile

def test_register_user():
    print("Testing register_user()...")
    register_user("registest", 'test', 'test@test.test', 'firstest', 'lastest', 'male', 'tuesday')
    user = find_by_username('registest')
    assert user.username == 'registest' and user.password == 'test' and user.email == 'test@test.test' and user.first_name == 'firstest' and user.last_name == 'lastest' and user.gender == 'male' and user.dob=='tuesday' and user.status =='Available' and user.imgpath == 'default.jpg' and user.degree == 'None' and user.flags == -1 and user.last_update == -1
    print("register_user() OK!")
    
def test_delete_user():
    print("Testing delete_user()...")
    delete_account_sql(get_user_id_from_username("registest"))
    user = find_by_username('registest')
    assert user is None
    print("delete_user() OK!")

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
    services.SQLService.connect()
    test_register_user()
    test_delete_user()
    test_find_by_email_pass()
    test_find_by_email()
    test_find_by_username()
    test_find_by_id()
    test_update_user()
    test_get_user_id_from_username()
    test_get_username_from_user_id()
    services.SQLService.disconnect()
except:
    update_user(2, username='service', password='service', firstname='servicefirst', lastname='servicelast', email='service@service.com', gender='servicegender', dob='servicedob', status='Available', imgpath='default.jpg', degree='Computer Science')
    services.SQLService.disconnect()
    assert False
print("==UserProfileService.py OK!==")
