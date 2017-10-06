import time
from flask import Flask, render_template, url_for, redirect, request, session
from services.UserProfileService import *
from services.MeetUpRequestService import *
from services.FriendRequestService import *

import utilities.profile

from flask import Flask, render_template, url_for
app = Flask(__name__)
app.secret_key = "secret-key"


@app.route("/")
def index():
    if (session.get("loggedInUser") is not None):
        return redirect(url_for('available'))
    else:
        return render_template("signin.html")


@app.route("/login", methods=['POST'])
def login():
    username = request.form["inputEmail"]
    password = request.form["inputPassword"]
    profile = find_by_email_pass(username, password)
    if (profile is not None):
        session['loggedInUser'] = profile.user_id
        return redirect(url_for('available'))
    else:
        return render_template("signin.html", error_message="Incorrect username or password")


@app.route("/logout")
def logout():
    session.pop('loggedInUser', None)
    session.clear()
    return render_template("signin.html")


@app.route("/register", methods=['POST'])
def register():
    username = request.form["username"]
    password = request.form["password"]
    email = request.form["email"]
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    gender = request.form["gender"]
    dob = request.form["dob"]

    errors = []
    existing_user = find_by_email(email)
    if (existing_user is not None):
        errors.append("That username has been taken already")
    existing_user = find_by_username(username)
    if (existing_user is not None):
        errors.append("That username has been taken already")

    if (len(errors) > 0):
        return render_template("register.html", register_error=", ".join(errors))

    register_user(username, password, email, firstname, lastname, gender, dob)
    return render_template("created.html")


@app.route("/registerPage")
def displaySignIn():
    return render_template("register.html")


@app.route('/available')
def available():
    # TODO: get list of logged-in user's friends that are available
    friends_of_user = friends_by_profile(session.get("loggedInUser"))

    available = [
        {
         'user_id': p.user_id,
         'first_name': p.first_name,
         'last_name': p.last_name,
         'username': p.username,
         'imgpath': p.imgpath
         } for p in friends_of_user
        if p.status == utilities.profile.statuses[0]
    ]

    logged_in_user = find_by_id(session.get("loggedInUser"))

    notifications = load_notifications(session.get("loggedInUser"))
    friends_notifications = load_friend_notifications(session.get("loggedInUser"))
    print(session.get("loggedInUser"))
    sender_dict = map_sender_to_user(notifications)
    sender_dict.update(map_sender_to_user(friends_notifications))
    receiver_dict = map_receiver_to_user(notifications)
    receiver_dict.update(map_receiver_to_user(friends_notifications))
    print(receiver_dict)
    return render_template('available.html', logged_in_user=logged_in_user, available=available,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)


@app.route('/todo')
def todo():
    todo_list = load_todos(session.get("loggedInUser"))
    tasks = []
    for task in todo_list:
        tasks += [
            {
                'id': task['id'],
                'name': task['title'],
                'text': task['description'],
                'subject': task['course_name'],
                'date': task['end_time']
            }
        ]

    logged_in_user = find_by_id(session.get("loggedInUser"))

    notifications = load_notifications(session.get("loggedInUser"))
    print(session.get("loggedInUser"))
    sender_dict = map_sender_to_user(notifications)
    receiver_dict = map_receiver_to_user(notifications)
    return render_template('todo.html', logged_in_user=logged_in_user, tasks=tasks, notifications=notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)

@app.route('/showPublicEvents')
def showPublicEvents():
    logged_in_user = find_by_id(session.get("loggedInUser"))

    tasks = load_public_events()
    notifications = load_notifications(session.get("loggedInUser"))
    sender_dict = map_sender_to_user(notifications)
    receiver_dict = map_receiver_to_user(notifications)
    return render_template('publicevents.html', logged_in_user=logged_in_user, tasks=tasks, notifications=notifications,
                           sender_dict=sender_dict, receiver_dict=receiver_dict)

@app.route("/todo/createPublicEvent", methods=['POST', 'GET'])
def todo_create_public_event():
    add_todo("idk",request.args.get("title"), request.args.get("description"), str(session.get("loggedInUser")), "PUBLIC", request.args.get("startTime"), request.args.get("endTime"))
    return todo()

@app.route("/todo/create", methods=['POST'])
def todo_create():
    add_todo("a", request.form["title"], request.form["description"], str(session.get("loggedInUser")),
             request.form["course"], str(time.time()), request.form["date"])
    return todo()


@app.route('/todo/delete/<todo_id>')
def todo_delete(todo_id):
    delete_todo(todo_id)
    return todo()


def get_busy_times(courses):
    busy_times = []
    for course in courses:
        for i in range(course['length']):
            busy_times.append({'day': course['day'], 'time': course['time']+i})
    return busy_times


@app.route('/user/<username>', methods=['GET'])
def user(username):

    friends_of_user = friends_by_id(session.get("loggedInUser"))

    user = find_by_username(username)

    courses = timetable_by_username(username)

    busy_times = get_busy_times(courses)

    logged_in_user = find_by_id(session.get("loggedInUser"))

    notifications = load_notifications(session.get("loggedInUser"))
    print(session.get("loggedInUser"))

    sender_dict = map_sender_to_user(notifications)
    receiver_dict = map_receiver_to_user(notifications)
    return render_template('user.html', logged_in_user=logged_in_user, user=user, friends_of_user=friends_of_user, courses=courses, busy_times=busy_times, notifications=notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)


@app.route("/class/create", methods=['POST'])
def class_create():

    user_id = str(session.get("loggedInUser"))
    course_name = request.form["course"]
    start_time = request.form["time"][:-3]

    day_numbers = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}
    day = day_numbers[request.form["day"]]

    length = request.form["length"]
    activity = request.form["activity"]


    add_class(user_id, course_name, start_time, day, length, activity)

    logged_in_user = get_username_from_user_id(session.get("loggedInUser"))
    return redirect(url_for('user', username=logged_in_user))

@app.route('/class/delete/<class_id>')
def class_delete(class_id):
    delete_class(class_id)
    logged_in_user = get_username_from_user_id(session.get("loggedInUser"))
    return redirect(url_for('user', username=logged_in_user))

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    logged_in_user = find_by_id(session.get("loggedInUser"))
    error_message = ''
    if request.method == 'POST':
        old_pw = request.form.get('input-old-password')
        if old_pw == logged_in_user.password:
            new_username = request.form.get('input-username')
            if not utilities.profile.change_username(logged_in_user, new_username):
                error_message += 'Username already taken.'
            new_password = request.form.get('input-new-password')
            utilities.profile.change_password(logged_in_user, new_password)            
            new_email = request.form.get('input-email')
            if not utilities.profile.change_email(logged_in_user, new_email):
                error_message += ('\nEmail already taken.' if error_message else 'Email already taken.')            
            new_status = request.form.get('input-status')
            utilities.profile.change_status(logged_in_user, new_status)
            new_firstname = request.form.get('input-firstname')
            utilities.profile.change_firstname(logged_in_user, new_firstname)
            new_lastname = request.form.get('input-lastname')
            utilities.profile.change_lastname(logged_in_user, new_lastname)
            new_gender = request.form.get('input-gender')
            utilities.profile.change_gender(logged_in_user, new_gender)
            new_dob = request.form.get('input-dob')
            utilities.profile.change_dob(logged_in_user, new_dob)
            new_degree = request.form.get('input-degree')
            utilities.profile.change_degree(logged_in_user, new_degree)
        else:
            error_message = 'Incorrect password.'

    notifications = load_notifications(session.get("loggedInUser"))
    print(session.get("loggedInUser"))
    sender_dict = map_sender_to_user(notifications)
    receiver_dict = map_receiver_to_user(notifications)
    return render_template('settings.html', logged_in_user=logged_in_user, statuses=utilities.profile.statuses, notifications=notifications, sender_dict=sender_dict, receiver_dict=receiver_dict, error_message=error_message)


@app.route("/search", methods=['GET'])
def user_search():
    # get arguments
    search_query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)
    # set how many results per page
    per_page = 1

    profiles = []
    # if query exists
    if search_query:
        results = search_users(search_query)
        profiles = [
            { 'first_name': p['firstname'],
              'last_name': p['lastname'],
              'username': p['username'],
              'imgpath': p['imgpath']
            } for p in results
        ]

    # split output into how many per page
    output = [profiles[i:i + per_page] for i in range(0, len(profiles), per_page)]
    page_count = len(output)
    # if arguments out of range reset them
    if page > len(output):
        page = len(output)
    elif page <= 0:
        page = 1

    # if no results found, set to empty array
    if len(output) == 0:
        users = []
    else:
        users = output[page - 1]

    logged_in_user = find_by_id(session.get("loggedInUser"))
    notifications = load_notifications(session.get("loggedInUser"))
    print(session.get("loggedInUser"))
    sender_dict = map_sender_to_user(notifications)
    receiver_dict = map_receiver_to_user(notifications)
    return render_template('search.html', logged_in_user=logged_in_user, search=search_query, results=users, page=page, count=len(profiles), page_count=page_count, notifications=notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)


def load_notifications(user_id):
    notifications = find_user_requests(user_id)
    notifications.extend(find_user_accepted_requests(user_id))
    notifications.extend(find_user_rejected_requests(user_id))
    return notifications

def map_sender_to_user(notifications):
    map = {}
    for n in notifications:
        map[n.from_id] = find_by_id(n.from_id)
    return map

def map_receiver_to_user(notifications):
    map = {}
    for n in notifications:
        map[n.to_id] = find_by_id(n.to_id)
    return map

@app.route('/sendFriendRequest', methods=['POST', 'GET'])
def send_friend_request():
    print("Hello")
    from_user_id = session.get("loggedInUser")
    to_user_id = request.form["userId"]
    message = request.form["message"]
    now = datetime.datetime.now()
    now = now.strftime("%Y-%m-%d")
    print(now)
    send_friend_request_db(from_user_id, to_user_id, message, now)

    return redirect(url_for('available'))

@app.route('/acceptFriendRequest', methods=['POST','GET'])
def accept_friend_request():
    to_user_id = session.get("loggedInUser")
    from_user_id = request.args.get("userId")
    accept_friend_request_db(from_user_id, to_user_id)
    return redirect(url_for('available'))

@app.route('/rejectFriendRequest', methods=['POST', 'GET'])
def reject_friend_request():
    to_user_id = session.get("loggedInUser")
    from_user_id = request.args.get("userId")
    reject_friend_request_db(from_user_id, to_user_id)
    return redirect(url_for('available'))

def load_friend_notifications(user_id):
    friend_notifications = find_friend_requests(user_id)
    friend_notifications.extend(find_user_accepted_friend_requests(user_id))
    return friend_notifications

@app.route('/sendMeetUpRequest', methods=['POST', 'GET'])
def send_meetup_request():
    from_user_id = session.get("loggedInUser")
    to_user_id = request.form["userId"]
    date = request.form["date"]
    time = request.form["time"]
    date_time = date + " " + time
    description = request.form["description"]
    send_request(from_user_id, to_user_id, description, date_time)

    return redirect(url_for('available'))

@app.route('/acceptMeetUpRequest', methods=['POST','GET'])
def accept_meetup_request():
    to_user_id = session.get("loggedInUser")
    from_user_id = request.args.get("userId")
    accept_request(from_user_id, to_user_id)
    return redirect(url_for('available'))

@app.route('/rejectMeetUpRequest', methods=['POST', 'GET'])
def reject_meetup_request():
    to_user_id = session.get("loggedInUser")
    from_user_id = request.args.get("userId")
    reject_request(from_user_id, to_user_id)
    return redirect(url_for('available'))

@app.errorhandler(404)
def page_not_found(e):
    return '404 <button onclick="window.history.back()">Go Back</button>', 404


if __name__ == '__main__':
    app.run(debug=True)
