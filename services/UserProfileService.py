import time
import datetime
from services.SQLService import *

from classes.UserProfile import UserProfile
from classes.PublicEvent import PublicEvent

import utilities.profile


def load_profile(sql_row):
    return UserProfile(sql_row["id"], sql_row["username"], sql_row["password"], sql_row["firstname"], sql_row["lastname"], sql_row["email"], sql_row["gender"], sql_row["dob"], sql_row["status"], sql_row["imgpath"], sql_row["degree"],
                       sql_row["flags"], sql_row["last_update"])


def all_users():
    sql = "SELECT * FROM user_profile"
    table = execute_sql(sql)
    return [load_profile(row) for row in table]

def friends_by_id(user_id):
    sql = "SELECT * FROM user_friend WHERE user_id1="+str(user_id)
    table = execute_sql(sql)
    profiles = []
    for row in table:
        profile = find_by_id(row["user_id2"])
        if profile not in profiles:
            profiles.append(profile)

    sql = "SELECT * FROM user_friend WHERE user_id2="+str(user_id)
    table = execute_sql(sql)
    for row in table:
        profile = find_by_id(row["user_id1"])
        if profile not in profiles:
            profiles.append(profile)
    return profiles

def pending_friends_by_id(user_id):
    sql = "SELECT * FROM friend_request WHERE from_id="+str(user_id)+" AND status='PENDING'"
    table = execute_sql(sql)
    profiles = []
    for row in table:
        profile = find_by_id(row["to_id"])
        if profile not in profiles:
            profiles.append(profile)
    return profiles

#Retreives a user based on email and pass
def find_by_email_pass(email, password):
    sql = "SELECT * FROM user_profile WHERE email = '" + email + "' AND password = '" + password + "'"
    table = execute_sql(sql)
    profile = None
    for row in table:
        profile = load_profile(row)
    return profile

#Retreives a user based on user and pass
def find_by_user_pass(user, password):
    sql = "SELECT * FROM user_profile WHERE username = '" + user + "' AND password = '" + password + "'"
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
    sql = "INSERT INTO user_profile(id, username, password, firstname, lastname, email, gender, dob, status, imgpath, degree, flags, last_update) VALUES (null, '" + username + "', '" + password + "', '" + firstname + "', '" + lastname + "', '" + email + "', '" + gender + "', '" + dob + "', '" + utilities.profile.statuses[0] + "', 'default.jpg', 'None', -1, -1)"
    table = execute_sql(sql)


#updates a user on given parameters
def update_user(user_id, username=None, password=None, email=None, firstname=None, lastname=None, gender=None, dob=None, status=None, imgpath=None, degree=None, flags=None, last_update=None):
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
    if not flags is None:
        sql += "flags = " + str(flags) + ", "
    if not last_update is None:
        sql += "last_update = " + str(last_update) + ", "

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


def timetable_by_id(user_id):
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


def timetable_by_username(username):
    user_id = get_user_id_from_username(username)
    return timetable_by_id(user_id)


def load_todos(id):
    sql = "SELECT * FROM user_todo_list WHERE user_id = " + str(id)
    table = execute_sql(sql)
    todo_list = list(table.fetchall())
    return todo_list


def update_todos(todos):
    sql = ""
    for key, value in todos.items():
        if int(value) > 3 or int(value) < -1:
            return False
        elif int(value) == -1:
            sql += "DELETE FROM user_todo_list WHERE id = " + str(key) + ";"
        else:
            sql += "UPDATE user_todo_list SET priority = " + value + " WHERE id = " + str(key) + ";"
    execute_sql(sql)
    return True


def load_public_events():
    sql = "SELECT * FROM public_event"
    table = execute_sql(sql)
    public_events = list(table.fetchall())
    return public_events


def add_public_events(id, title, description, start_time, end_time):
    sql = "INSERT INTO public_event(id, title, description, start_time, end_time) VALUES (null, '" + title + "', '" + description + "', '" + start_time + "', '" + end_time + "')"
    table = execute_sql(sql)


def add_todo(id, title, description, user_id, course_name, create_time, end_time, priority):
    sql = "INSERT INTO user_todo_list(id, title, description, user_id, course_name, create_time, end_time, priority) VALUES (null, '" + title + "', '" + description + "', '" + user_id + "', '" + course_name + "', '" + create_time + "', '" + end_time + "', '" + priority + "')"
    table = execute_sql(sql)


def add_class(user_id, course_name, start_time, day, length, activity):
    sql = "insert into user_class (user_id, course_name, start_time, day, length, activity) values ({}, '{}', {}, {}, {}, '{}')".format(user_id, course_name, start_time, day, length, activity)
    table = execute_sql(sql)


def search_users(query):
    # search users based on query
    # concat both first name and last name, search last name only, search first name only
    sql = "SELECT * FROM user_profile WHERE CONCAT(firstname, ' ', lastname) LIKE '%s%%' OR lastname LIKE '%s%%' OR firstname LIKE '%s%%'" % (query, query, query)
    table = execute_sql(sql)
    user_list = list(table.fetchall())
    return user_list


def delete_class(id):
    sql = "DELETE FROM user_class WHERE id = " + str(id)
    table = execute_sql(sql)


def delete_account_sql(id):
    sql = "DELETE FROM user_friend WHERE user_id1 = " + str(id)\
          + ";DELETE FROM friend_request WHERE from_id = " + str(id) \
          + ";DELETE FROM friend_request WHERE to_id = " + str(id) \
          + ";DELETE FROM user_friend WHERE user_id2 = " + str(id) \
          + ";DELETE FROM user_meetup_request WHERE from_id = " + str(id) \
          + ";DELETE FROM user_meetup_request WHERE to_id = " + str(id) \
          + ";DELETE FROM user_class WHERE user_id = " + str(id) +\
          ";DELETE FROM user_todo_list WHERE user_id = " + str(id) + \
          ";DELETE FROM user_profile WHERE id = " + str(id)
    table = execute_sql(sql)


def all_courses():
    sql = "SELECT DISTINCT faculty, course_code, class_id FROM courses"
    table = execute_sql(sql)
    courses = []
    for row in table:
        courses.append({
            'course_code': '{}{}'.format(row['faculty'], row['course_code']),
            'class_id': row['class_id']
        })
    return courses


def courses_on_code_and_id(course_code, class_id):
    faculty = course_code[:4]
    course_code = course_code[4:]
    sql = "SELECT * FROM courses WHERE faculty = '{}' AND course_code = {} AND class_id = '{}'".format(faculty, course_code, class_id)
    table = execute_sql(sql)
    courses = []
    for row in table:
        courses.append({
            'course_code': '{}{}'.format(row['faculty'], row['course_code']),
            'class_id': row['class_id'],
            'day': row['day'],
            'activity': row['activity'],
            'start_time': row['start_time'],
            'length': row['length']
        })
    return courses

def find_common_courses(user_id):
    recommended = {}
    sql = "select distinct user_id, course_name FROM user_class WHERE course_name IN (SELECT course_name FROM user_class WHERE user_id = " + str(user_id) + ") AND user_id != " + str(user_id);
    table = execute_sql(sql)
    for row in table:
        if (row['user_id'] not in recommended):
            recommended[row['user_id']] = [];
        recommended[row['user_id']].append(row['course_name'])

    return recommended

def doing_course(course):
    students = []
    sql = "SELECT DISTINCT user_id FROM user_class WHERE course_name = '{}'".format(course)
    table = execute_sql(sql)
    for row in table:
        students.append(row['user_id'])

    return students

#grabs all the users that have the same friends as u
def find_users_with_mutual_friends(user_id):
    mutual_friends = {}
    sql = ""
    sql +=      "select user_id1 as friend from"
    sql +=          "("
    sql +=	            "select * from user_friend where (user_id1 IN "
    sql +=		            "("
    sql +=			            "select user_id2 as friend FROM user_friend where user_id1 = " + str(user_id)
    sql +=			            " UNION "
    sql +=			            "select user_id1 as friend FROM user_friend where user_id2 = " + str(user_id)
    sql +=		            ") or user_id2 in "
    sql +=		            "("
    sql +=			            "select user_id2 as friend FROM user_friend where user_id1 = " + str(user_id)
    sql +=			            " UNION "
    sql +=			            "select user_id1 as friend FROM user_friend where user_id2 = " + str(user_id)
    sql +=		            ")"
    sql +=	            ") and user_id1 != " + str(user_id) + " and user_id2 != " + str(user_id)
    sql +=          ") as friends where user_id2 in "
    sql +=              "("
    sql +=                  "select user_id2 as friend FROM user_friend where user_id1 = " + str(user_id)
    sql +=                  " UNION "
    sql +=                  "select user_id1 as friend FROM user_friend where user_id2 = " + str(user_id)
    sql +=                ")"
    sql +=      " UNION "
    sql +=      "select user_id2 as friend from"
    sql +=           "("
    sql +=                "select * from user_friend where (user_id1 in "
    sql +=                  "("
    sql +=                       "select user_id2 as friend FROM user_friend where user_id1 = " + str(user_id)
    sql +=                        " UNION "
    sql +=                       " select user_id1 as friend FROM user_friend where user_id2 = " + str(user_id)
    sql +=                   ") or user_id2 in "
    sql +=                   "("
    sql +=                        "select user_id2 as friend FROM user_friend where user_id1 = " + str(user_id)
    sql +=                        " UNION "
    sql +=                        "select user_id1 as friend FROM user_friend where user_id2 = " + str(user_id)
    sql +=                   ")"
    sql +=                ") and user_id1 != " + str(user_id) + " and user_id2 != " + str(user_id)
    sql +=             ") as friends where user_id1 in "
    sql +=                 "("
    sql +=                    "select user_id2 as friend FROM user_friend where user_id1 = " + str(user_id)
    sql +=                    " UNION "
    sql +=                    "select user_id1 as friend FROM user_friend where user_id2 = " + str(user_id)
    sql +=                  ")"
    table = execute_sql(sql)
    for row in table:
        mutual_friends[row["friend"]] = [];
    for key, value in mutual_friends.items():
        sql = "select user_id1 as friend from user_friend where user_id1 in "
        sql +=    "(select user_id1 from user_friend where user_id2 = " + str(user_id)
        sql +=    " union "
        sql +=    "select user_id2 from user_friend where user_id1 = " +str(user_id) +") "
        sql +=    "and user_id2="+str(key)
        sql += " union "
        sql += "select user_id2 as friend from user_friend where user_id2 in "
        sql +=    "(select user_id1 from user_friend where user_id2 = " + str(user_id)
        sql +=    " union "
        sql +=    "select user_id2 from user_friend where user_id1 =" +str(user_id) +") "
        sql +=    "and user_id1=" + str(key)
        table = execute_sql(sql)
        for row in table:
            user = find_by_id(row['friend'])
            mutual_friends[key].append(user)
    return mutual_friends

def update_img_path(username):
    sql = "UPDATE user_profile SET imgpath = '" + username + ".png' WHERE username='" + username + "'"
    table = execute_sql(sql)


def string_to_date(string):
    try:
        date = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M").strftime("%d/%m/%Y, %A %I:%M %p")
    except ValueError:
        return string
    return date
