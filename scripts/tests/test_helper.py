#!/usr/local/bin/python3.6
import pymysql

from services.UserProfileService import load_profile
        
def get_test_profile():
    print("=== Retrieving dummy user... ===")
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195386', password='yLV5WQ5Lx5', db='sql12195386', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_profile WHERE username = 'dummyname'"
            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                profile = load_profile(row)
            print("=== Retrieved dummy user ===")
    finally:
        # Close connection.
        connection.close()
    return profile