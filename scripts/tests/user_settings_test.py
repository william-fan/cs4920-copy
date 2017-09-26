#!/usr/local/bin/python3.6
import sys
sys.path.append('./')
from status import *
from services.UserProfileService import *
import classes.UserProfile

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
    
print("==Testing user profile settings...==")
test_change_status()
print("==User profile settings OK!==")