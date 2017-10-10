from services.SQLService import *

from classes.MeetUpRequest import MeetUpRequest


def find_user_requests(receiver_id):
    requests = []
    sql = "SELECT * FROM user_meetup_request WHERE to_id = " + str(receiver_id) + " AND status = 'PENDING'"
    table = execute_sql(sql)
    for row in table:
        requests.append(MeetUpRequest(row["from_id"], row["to_id"], row["status"], row["description"], row["date"]))
    return requests

def find_user_accepted_requests(sender_id):
    requests = []
    sql = "SELECT * FROM user_meetup_request WHERE from_id = " + str(sender_id) + " AND status = 'ACCEPTED'"
    table = execute_sql(sql)
    for row in table:
        requests.append(MeetUpRequest(row["from_id"], row["to_id"], row["status"], row["description"], row["date"]))
    return requests

def find_user_rejected_requests(sender_id):
    requests = []
    sql = "SELECT * FROM user_meetup_request WHERE from_id = " + str(sender_id) + " AND status = 'REJECTED'"
    table = execute_sql(sql)
    for row in table:
        requests.append(MeetUpRequest(row["from_id"], row["to_id"], row["status"], row["description"], row["date"]))
    return requests


def accept_request(from_id, to_id):
    sql = "UPDATE user_meetup_request SET status = 'ACCEPTED' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)

def reject_request(from_id, to_id):
    sql = "UPDATE user_meetup_request SET status = 'ACCEPTED' WHERE from_id = " + str(
        from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)


def send_request(from_id, to_id, description, date_time):
    sql = "INSERT INTO user_meetup_request(from_id, to_id, status, description, date) VALUES ('" + str(from_id) + "', '" + str(to_id) + "', '" + 'PENDING' + "', '" + description + "', '" + date_time + "')"
    table = execute_sql(sql)


