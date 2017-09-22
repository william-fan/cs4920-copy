import pymysql

from classes.UserProfile import UserProfile
from classes.ToDo import ToDo

import status

def load_profile(sql_row):
    return UserProfile(sql_row["id"], sql_row["username"], sql_row["password"], sql_row["firstname"], sql_row["lastname"], sql_row["email"], sql_row["gender"], sql_row["dob"], sql_row["status"], sql_row["imgpath"])

def friends_by_id(user_id):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    profiles = []
    try:
        with connection.cursor() as cursor:
            #TODO: Actually retrieve a list of user's friends.
            # Currently returns all users.
            # SQL
            sql = "SELECT * FROM user_profile"

            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                if row["id"] != user_id:
                    profiles.append(load_profile(row))
    finally:
        # Close connection.
        connection.close()
    return profiles

#Retreives a user based on email and pass
def find_by_email_pass(email, password):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    profile = None
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_profile WHERE email = '" + email + "' AND password = '" + password + "'"

            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                profile = load_profile(row)

    finally:
        # Close connection.
        connection.close()
    return profile

#Retreives a user based on email and pass
def find_by_email(email):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    profile = None
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_profile WHERE email = '" + email + "'"

            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                profile = load_profile(row)

    finally:
        # Close connection.
        connection.close()
    return profile

def find_by_username(username):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    profile = None
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_profile WHERE username = '" + username + "'"

            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                profile = load_profile(row)

    finally:
        # Close connection.
        connection.close()
    return profile

#Retrieves a user based on their id
def find_by_id(id):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    profile = None
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_profile WHERE id = " + str(id)

            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                profile = load_profile(row)

    finally:
        # Close connection.
        connection.close()
    return profile

#registers a user
def register_user(username, password, email, firstname, lastname, gender, dob):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058', password='WWCl5DaAea', db='sql12195058', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "INSERT INTO user_profile(id, username, password, firstname, lastname, email, gender, dob, status, imgpath) VALUES (null, '" + username + "', '" + password + "', '" + firstname + "', '" + lastname + "', '" + email + "', '" + gender + "', '" + dob + "', '" + status.statuses[0] + "', 'default.jpg')"

            # Execute query.
            cursor.execute(sql)
            connection.commit()

    finally:
        # Close connection.
        connection.close()


def load_todos(id):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    todo_list = ()
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_todo_list WHERE user_id = " + str(id)

            # Execute query.
            cursor.execute(sql)

            todo_list = list(cursor.fetchall())

    finally:
        # Close connection.
        connection.close()
    return todo_list

#add a to-do for a user
def add_todo(id, title, description, user_id, course_name, create_time, end_time):

    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058', password='WWCl5DaAea', db='sql12195058', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor, autocommit=True)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "INSERT INTO user_todo_list(id, title, description, user_id, course_name, create_time, end_time) VALUES (null, '" + title + "', '" + description + "', '" + user_id + "', '" + course_name + "', '" + create_time + "', '" + end_time + "')"

            # Execute query.
            cursor.execute(sql)
            connection.commit()

    finally:
        # Close connection.
        connection.close()