from services.SQLService import *
import datetime

from classes.FriendRequest import FriendRequest

def find_friend_requests(receiver_id):
    requests = []
    sql = "SELECT * FROM friend_request WHERE to_id = " + str(receiver_id) + " AND status = 'PENDING'"
    table = execute_sql(sql)
    for row in table:
        requests.append(FriendRequest(row["from_id"], row["to_id"], row["status"], row["message"], row["date"]))
    return requests

def find_user_accepted_friend_requests(sender_id):
    requests = []
    sql = "SELECT * FROM friend_request WHERE from_id = " + str(sender_id) + " AND status = 'ACCEPTED'"
    table = execute_sql(sql)
    for row in table:
        requests.append(FriendRequest(row["from_id"], row["to_id"], row["status"], row["message"], row["date"]))
    return requests


def accept_friend_request_db(from_id, to_id):
    sql = "UPDATE friend_request SET status = 'ACCEPTED' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    sql = "UPDATE friend_request SET date = '" + now + "' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)
    sql = "INSERT INTO user_friend(user_id1, user_id2) VALUES(" + str(from_id) + ", " + str(to_id) + ")"
    table = execute_sql(sql)
    sql = "INSERT INTO user_friend(user_id1, user_id2) VALUES(" + str(to_id) + ", " + str(from_id) + ")"
    table = execute_sql(sql)

def reject_friend_request_db(from_id, to_id):
    sql = "UPDATE friend_request SET status = 'REJECTED' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    sql = "UPDATE friend_request SET date = '" + now + "' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)


def send_friend_request_db(from_id, to_id, message,now):
    sql = "INSERT INTO friend_request(from_id, to_id, status, message, date) VALUES(" + str(from_id) + ", " + str(to_id) + ", 'PENDING', '" + message + "', '" + str(now) + "')"
    table = execute_sql(sql)

def delete_friend_request_db(from_id, to_id):
    sql = "DELETE FROM friend_request WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)

def remove_friend_from_db(user_id1, user_id2):
    print("user 1")
    print(user_id1)
    print("user 2")
    print(user_id2)
    sql ="DELETE FROM user_friend WHERE user_id1=\"" + str(user_id1) + "\" AND user_id2=\"" + str(user_id2) + "\""
    table = execute_sql(sql)
    sql ="DELETE FROM user_friend WHERE user_id1=\"" + str(user_id2) + "\" AND user_id2=\"" + str(user_id1) + "\""
    table = execute_sql(sql)
