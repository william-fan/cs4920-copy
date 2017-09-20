#!/usr/local/bin/python3.6
import sys
sys.path.append('./')
sys.path.append('./scripts/tests')
from test_helper import get_test_profile
from status import *
import classes.UserProfile

def test_change_status():
    print("Testing status changing...")
    user = get_test_profile()
    for status in statuses:
        change_status(user, status)
        assert user.status == status

test_change_status()