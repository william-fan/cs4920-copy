import time
import datetime
from services.SQLService import *

from classes.MeetUpRequest import MeetUpRequest
from services.UserProfileService import *


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
    from_user = find_by_id(from_id)
    to_user = find_by_id(to_id)
    from_name = from_user.first_name + " " + from_user.last_name
    to_name = to_user.first_name + " " + to_user.last_name
    sql = "UPDATE user_meetup_request SET status = 'ACCEPTED' WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)
    sql = "SELECT * FROM user_meetup_request WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id) + " AND status = 'ACCEPTED'"
    table = execute_sql(sql)
    for row in table:
        sql = "INSERT INTO user_todo_list(id, title, description, user_id, course_name, create_time, end_time, priority) VALUES (null, 'Meet Up With Friend', '" + row["description"] + "', '" + str(from_id) + "', '" + to_name + "', '" + string_to_date(row["date"]) + "', '" + string_to_date(row["date"]) + "', '1')"
        table = execute_sql(sql)
        sql = "INSERT INTO user_todo_list(id, title, description, user_id, course_name, create_time, end_time, priority) VALUES (null, 'Meet Up With Friend', '" + row["description"] + "', '" + str(to_id) + "', '" + from_name + "', '" + string_to_date(row["date"]) + "', '" + string_to_date(row["date"]) + "', '1')"
        table = execute_sql(sql)



def reject_request(from_id, to_id):
    sql = "UPDATE user_meetup_request SET status = 'ACCEPTED' WHERE from_id = " + str(
        from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)


def send_request(from_id, to_id, description, date_time):
    sql = "INSERT INTO user_meetup_request(from_id, to_id, status, description, date) VALUES ('" + str(from_id) + "', '" + str(to_id) + "', '" + 'PENDING' + "', '" + description + "', '" + date_time + "')"
    table = execute_sql(sql)

def delete_request(from_id, to_id):
    sql = "DELETE FROM user_meetup_request WHERE from_id = " + str(from_id) + " AND to_id = " + str(to_id)
    table = execute_sql(sql)


def string_to_date(string):
    try:
        date = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M").strftime("%d/%m/%Y, %A %I:%M %p")
    except ValueError:
        return string
    return date