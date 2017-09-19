import pymysql
from classes.UserProfile import UserProfile

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
                profile = UserProfile(row["id"], row["username"], row["password"], row["firstname"], row["lastname"], row["email"], row["gender"], row["dob"], row["status"], row["imgpath"])

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
                profile = UserProfile(row["id"], row["username"], row["password"], row["firstname"], row["lastname"], row["email"], row["gender"], row["dob"], row["status"], row["imgpath"])

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
                profile = UserProfile(row["id"], row["username"], row["password"], row["firstname"], row["lastname"], row["email"], row["gender"], row["dob"], row["status"], row["imgpath"])

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
                profile = UserProfile(row["id"], row["username"], row["password"], row["firstname"], row["lastname"], row["email"], row["gender"], row["dob"], row["status"], row["imgpath"])

    finally:
        # Close connection.
        connection.close()
    return profile

#registers a user
def register_user(username, password, email, firstname, lastname, gender, dob):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058', password='WWCl5DaAea', db='sql12195058', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "INSERT INTO user_profile(id, username, password, firstname, lastname, email, gender, dob, status, imgpath) VALUES (null, '" + username + "', '" + password + "', '" + firstname + "', '" + lastname + "', '" + email + "', '" + gender + "', '" + dob + "', 'CREATED', 'default.jpg')"

            # Execute query.
            cursor.execute(sql)
            connection.commit()

    finally:
        # Close connection.
        connection.close()