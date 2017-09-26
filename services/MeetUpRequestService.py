import pymysql
import datetime
from classes.MeetUpRequest import MeetUpRequest

def find_user_requests(receiver_id):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    requests = []
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_meetup_request WHERE to_id = " + str(receiver_id) + " AND status = 'PENDING'"

            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                request = MeetUpRequest(row["from_id"], row["to_id"], row["status"], row["description"], row["date"])
                current_time = str(datetime.datetime.now()).split(".")[0] #extracts date in yyyy-mmm-dd hh:mm:ss format
                if (request.date < current_time):
                    continue

                requests.append(request)

    finally:
        # Close connection.
        connection.close()
    return requests

def find_user_accepted_requests(sender_id):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    requests = []
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_meetup_request WHERE from_id = " + str(sender_id) + " AND status = 'ACCEPTED'"

            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                request = MeetUpRequest(row["from_id"], row["to_id"], row["status"], row["description"], row["date"])
                requests.append(request)

    finally:
        # Close connection.
        connection.close()
    return requests

def find_user_rejected_requests(sender_id):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058',password='WWCl5DaAea', db='sql12195058',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
    requests = []
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "SELECT * FROM user_meetup_request WHERE from_id = " + str(sender_id) + " AND status = 'REJECTED'"

            # Execute query.
            cursor.execute(sql)

            for row in cursor:
                request = MeetUpRequest(row["from_id"], row["to_id"], row["status"], row["description"], row["date"])
                requests.append(request)

    finally:
        # Close connection.
        connection.close()
    return requests


def accept_request(from_id, to_id):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058', password='WWCl5DaAea', db='sql12195058', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "UPDATE user_meetup_request SET status = 'ACCEPTED' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)

            # Execute query.
            cursor.execute(sql)
            connection.commit()

    finally:
        # Close connection.
        connection.close()


def reject_request(from_id, to_id):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058', password='WWCl5DaAea', db='sql12195058', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "UPDATE user_meetup_request SET status = 'REJECTED' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)

            # Execute query.
            cursor.execute(sql)
            connection.commit()

    finally:
        # Close connection.
        connection.close()

def send_request(from_id, to_id, description, date):
    connection = pymysql.connect(host='sql12.freemysqlhosting.net', user='sql12195058', password='WWCl5DaAea', db='sql12195058', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            # SQL
            sql = "INSERT INTO user_meetup_request(from_id, to_id, status, description, date) VALUES (" + str(from_id) + ", " + str(to_id) + ", 'PENDING', '" + description + "', '" + date + "')"

            # Execute query.
            cursor.execute(sql)
            connection.commit()

    finally:
        # Close connection.
        connection.close()