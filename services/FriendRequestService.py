from services.SQLService import *

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
    sql = "INSERT INTO user_friend(user_id1, user_id2) VALUES(" + str(from_id) + ", " + str(to_id) + ")"
    table = execute_sql(sql)
    sql = "INSERT INTO user_friend(user_id1, user_id2) VALUES(" + str(to_id) + ", " + str(from_id) + ")"
    table = execute_sql(sql)

def reject_friend_request_db(from_id, to_id):
    sql = "UPDATE friend_request SET status = 'REJECTED' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)


def send_friend_request_db(from_id, to_id, message,now):
    sql = "INSERT INTO friend_request(from_id, to_id, status, message, date) VALUES(" + str(from_id) + ", " + str(to_id) + ", 'PENDING', '" + message + "', " + str(now) + ")"
    table = execute_sql(sql)
