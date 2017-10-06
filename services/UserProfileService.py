from services.SQLService import *

from classes.UserProfile import UserProfile
from classes.PublicEvent import PublicEvent
from classes.ToDo import ToDo

import utilities.profile


def load_profile(sql_row):
    return UserProfile(sql_row["id"], sql_row["username"], sql_row["password"], sql_row["firstname"], sql_row["lastname"], sql_row["email"], sql_row["gender"], sql_row["dob"], sql_row["status"], sql_row["imgpath"], sql_row["degree"])


def friends_by_id(user_id):
    sql = "SELECT * FROM user_friend WHERE user_id1="+str(user_id)
    table = execute_sql(sql)
    profiles = []
    for row in table:
        profiles.append(row["user_id2"])
    return profiles

def friends_by_profile(user_id):
    sql = "SELECT * FROM user_friend WHERE user_id1="+str(user_id)
    table = execute_sql(sql)
    profiles = []
    for row in table:
        profiles.append(find_by_id(row["user_id2"]))
    return profiles

#Retreives a user based on email and pass
def find_by_email_pass(email, password):
    sql = "SELECT * FROM user_profile WHERE email = '" + email + "' AND password = '" + password + "'"
    table = execute_sql(sql)
    profile = None
    for row in table:
        profile = load_profile(row)
    return profile


#Retreives a user based on email
def find_by_email(email):
    profile = None
    sql = "SELECT * FROM user_profile WHERE email = '" + email + "'"
    table = execute_sql(sql)
    for row in table:
        profile = load_profile(row)
    return profile


def find_by_username(username):
    profile = None
    sql = "SELECT * FROM user_profile WHERE username = '" + username + "'"
    table = execute_sql(sql)
    for row in table:
        profile = load_profile(row)
    return profile


#Retrieves a user based on their id
def find_by_id(id):
    profile = None
    sql = "SELECT * FROM user_profile WHERE id = " + str(id)
    table = execute_sql(sql)
    for row in table:
        profile = load_profile(row)
    return profile


#registers a user
def register_user(username, password, email, firstname, lastname, gender, dob):
    sql = "INSERT INTO user_profile(id, username, password, firstname, lastname, email, gender, dob, status, imgpath) VALUES (null, '" + username + "', '" + password + "', '" + firstname + "', '" + lastname + "', '" + email + "', '" + gender + "', '" + dob + "', '" + utilities.profile.statuses[0] + "', 'default.jpg')"
    table = execute_sql(sql)


#updates a user on given parameters
def update_user(user_id, username=None, password=None, email=None, firstname=None, lastname=None, gender=None, dob=None, status=None, imgpath=None, degree=None):
    sql = "UPDATE user_profile SET "
    if not username is None:
        sql += "username = '" + username + "', "
    if not password is None:
        sql += "password = '" + password + "', "
    if not email is None:
        sql += "email = '" + email + "', "
    if not firstname is None:
        sql += "firstname = '" + firstname + "', "
    if not lastname is None:
        sql += "lastname = '" + lastname + "', "
    if not gender is None:
        sql += "gender = '" + gender + "', "
    if not dob is None:
        sql += "dob = '" + dob + "', "
    if not status is None:
        sql += "status = '" + status + "', "
    if not imgpath is None:
        sql += "imgpath = '" + imgpath + "', "
    if not degree is None:
        sql += "degree = '" + degree + "', "

    # only do stuff if something was changed
    if sql != "UPDATE user_profile SET ":
        sql = sql[:-2] # take off the last comma and space
        sql += " WHERE id = " + str(user_id)
        table = execute_sql(sql)


def get_user_id_from_username(username):
    sql = "SELECT id FROM user_profile WHERE username = '" + username + "'"
    table = execute_sql(sql)
    user_id = None
    for row in table:
        user_id = row['id']
    return user_id


def get_username_from_user_id(user_id):
    sql = "SELECT username FROM user_profile WHERE id = {}".format(user_id)
    table = execute_sql(sql)
    username = None
    for row in table:
        username = row['username']
    return username


def timetable_by_username(username):
    user_id = get_user_id_from_username(username)
    sql = "SELECT * FROM user_class WHERE user_id = {}".format(user_id)
    table = execute_sql(sql)
    courses = []
    for row in table:
        courses.append({
            'id': row['id'],
            'day': row['day'],
            'time': row['start_time'],
            'length': row['length'],
            'subject': row['course_name'],
            'activity': row['activity']
        })
    return courses


def load_todos(id):
    sql = "SELECT * FROM user_todo_list WHERE user_id = " + str(id)
    table = execute_sql(sql)
    todo_list = list(table.fetchall())
    return todo_list

def load_public_events():
    public_events = []
    sql = "SELECT * FROM public_event"
    table = execute_sql(sql)
    for row in table:
        public_events.append(PublicEvent(row["id"], row["title"], row["description"], row["start_time"], row["end_time"]))

    return public_events


def add_todo(id, title, description, user_id, course_name, create_time, end_time):
    sql = "INSERT INTO user_todo_list(id, title, description, user_id, course_name, create_time, end_time) VALUES (null, '" + title + "', '" + description + "', '" + user_id + "', '" + course_name + "', '" + create_time + "', '" + end_time + "')"
    table = execute_sql(sql)


def delete_todo(id):
    sql = "DELETE FROM user_todo_list WHERE id = " + str(id)
    table = execute_sql(sql)


def add_class(user_id, course_name, start_time, day, length, activity):
    sql = "insert into user_class (user_id, course_name, start_time, day, length, activity) values ({}, '{}', {}, {}, {}, '{}')".format(user_id, course_name, start_time, day, length, activity)
    table = execute_sql(sql)


def search_users(query):
    # search users based on query
    # concat both first name and last name, search last name only, search first name only
    # unsanitised so far
    sql = "SELECT * FROM user_profile WHERE CONCAT(firstname, ' ', lastname) LIKE '%s%%' OR lastname LIKE '%s%%' OR firstname LIKE '%s%%'" % (query, query, query)
    table = execute_sql(sql)
    user_list = list(table.fetchall())
    return user_list

def delete_class(id):
    sql = "DELETE FROM user_class WHERE id = " + str(id)
    table = execute_sql(sql)
