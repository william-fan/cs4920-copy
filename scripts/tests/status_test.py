#!/usr/local/bin/python3.6
import sys
sys.path.insert(0, './classes/')
sys.path.insert(0, './')
from status import *
import UserProfile

newUser = UserProfile.UserProfile(None, None, None, None, None, None, None, None, None, Status.AVAILABLE, None)
print("Testing status changing...")
assert newUser.status == Status.AVAILABLE
change_status(newUser, Status.INCLASS)
assert newUser.status == Status.INCLASS
change_status(newUser, Status.OFFCAMPUS)
assert newUser.status == Status.OFFCAMPUS