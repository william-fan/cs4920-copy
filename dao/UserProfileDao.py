import pymysql
from classes.UserProfile import UserProfile

#Retreives a user based on email and pass
def findByEmailAndPass(email, password):
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

#Retrieves a user based on their id
def findById(id):
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

profile = findById(2)
print(profile.id)