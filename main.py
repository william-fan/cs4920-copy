import os
import json
from flask import Flask, render_template, url_for, redirect, request, session, send_from_directory
from services.UserProfileService import *
from services.MeetUpRequestService import *
from services.FriendRequestService import *
import services.SQLService

import utilities.profile

import datetime
from werkzeug.utils import secure_filename
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/img/users')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret-key"


def page_init():
    services.SQLService.connect()
    logged_in_user = find_by_id(session.get("loggedInUser"))
    notifications = load_notifications(session.get("loggedInUser"))
    friends_notifications = load_friend_notifications(session.get("loggedInUser"))
    sender_dict = map_sender_to_user(notifications)
    sender_dict.update(map_sender_to_user(friends_notifications))
    receiver_dict = map_receiver_to_user(notifications)
    receiver_dict.update(map_receiver_to_user(friends_notifications))

    return logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict

def page_init_lite():
    services.SQLService.connect()

def page_finish():
    services.SQLService.disconnect()


@app.route("/")
def index():
    if (session.get("loggedInUser") is not None):
        return redirect(url_for('home'))
    else:
        return render_template("signin.html")

@app.route("/home")
def home():
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()
    # utilities.profile.update_statuses(all_users())

    current_day = datetime.date.today().weekday()
    current_time = datetime.datetime.now().hour
    courses = timetable_by_username(logged_in_user.username)
    busy_times = get_busy_times(courses)

    friends_of_user = friends_by_id(session.get("loggedInUser"))
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

    todo_list = load_todos(session.get("loggedInUser"))
    tasks = []
    for task in todo_list:
        tasks += [
            {
                'id': task['id'],
                'name': task['title'],
                'text': task['description'],
                'subject': task['course_name'],
                'date': task['end_time'],
                'priority': task['priority']
            }
        ]


    page_finish()
    return render_template('home.html', logged_in_user=logged_in_user, available=available,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict, current_day=current_day, current_time=current_time, courses=courses, busy_times=busy_times, tasks=tasks)




@app.route("/login", methods=['POST'])
def login():
    username = request.form["inputUserEmail"]
    password = request.form["inputPassword"]
    profile = find_by_email_pass(username, password)
    if profile is not None:
        session['loggedInUser'] = profile.user_id
        return redirect(url_for('home'))
    profile = find_by_user_pass(username, password)
    if profile is not None:
        session['loggedInUser'] = profile.user_id
        return redirect(url_for('home'))
    else:
        return render_template("signin.html", error_message="Incorrect username or password")


@app.route("/logout")
def logout():
    session.pop('loggedInUser', None)
    session.clear()
    return render_template("signin.html")


@app.route("/register", methods=['POST'])
def register():
    page_init_lite()
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
        page_finish()
        return render_template("register.html", register_error=", ".join(errors))
    register_user(username, password, email, firstname, lastname, gender, dob)
    page_finish()
    return render_template("created.html")


@app.route("/registerPage")
def displaySignIn():
    return render_template("register.html")


@app.route('/todo')
def todo():
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()

    todo_list = load_todos(session.get("loggedInUser"))
    tasks = []
    for task in todo_list:
        tasks += [
            {
                'id': task['id'],
                'name': task['title'],
                'text': task['description'],
                'subject': task['course_name'],
                'date': task['end_time'],
                'priority': task['priority']
            }
        ]

    page_finish()
    return render_template('todo.html', logged_in_user=logged_in_user, tasks=tasks,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)


@app.route('/events')
def events():
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()

    event_list = load_public_events()
    tasks = []
    for task in event_list:
        tasks += [
            {
                'id': task['id'],
                'title': task['title'],
                'description': task['description'],
                'start_time': task['start_time'],
                'end_time': task['end_time']
            }
        ]

    page_finish()
    return render_template('publicevents.html', logged_in_user=logged_in_user, tasks=tasks,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)


@app.route("/events/create", methods=['POST', 'GET'])
def event_create():
    if request.method == 'POST':
        add_public_events("a", request.form["title"], request.form["description"],
                          string_to_date(request.form["startDate"]+" "+request.form["startTime"]),
                          string_to_date(request.form["endDate"]+" "+request.form["endTime"]))
    return events()


@app.route("/todo/createPublicEvent", methods=['GET'])
def todo_create_public_event():
    add_todo("a",request.args.get("title"), request.args.get("description"), str(session.get("loggedInUser")), "Event",
             string_to_date(request.args.get("startTime")), string_to_date(request.args.get("endTime")), "0")
    return todo()


@app.route("/todo/create", methods=['POST', 'GET'])
def todo_create():
    if request.method == 'POST':
        add_todo("a", request.form["title"], request.form["description"], str(session.get("loggedInUser")),
                 request.form["course"], datetime.datetime.now().strftime("%d/%m/%Y, %A %I:%M %p"),
                 string_to_date(request.form["date"]+" "+request.form["time"]), request.form["priority"])
    return todo()


@app.route("/todo/update", methods=['POST'])
def todo_update():
    todos = request.get_json()
    output = True
    if todos:
        output = update_todos(todos)
    if output:
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    else:
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'}


@app.route('/settings/delete_account', methods=['GET'])
def delete_account():
    confirmation = request.args.get("confirm")
    if confirmation == '1':
        delete_account_sql(session.get("loggedInUser"))
        return logout()
    else:
        return settings()


@app.route('/share', methods=['GET'])
def share():
    user_page = user(get_username_from_user_id(session.get("loggedInUser")))

    return user_page


def get_busy_times(courses):
    busy_times = []
    for course in courses:
        for i in range(course['length']):
            busy_times.append({'day': course['day'], 'time': course['time']+i})
    return busy_times


@app.route('/friends')
def friends():
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()

    friends_of_user = [profile.user_id for profile in friends_by_id(session.get("loggedInUser"))]
    friends_list = []
    for friend in friends_of_user:
        user = find_by_id(friend)
        course_list = set([])
        for courses in timetable_by_id(friend):
            course_list.add(courses['subject'])
        friends_list += [
            {
                'user_id': user.user_id,
                'imgpath': user.imgpath,
                'courses': sorted(course_list),
                'status': user.status,
                'name': user.first_name+" "+user.last_name,
                'username': user.username
            }
        ]

    page_finish()
    return render_template('friends.html', friends=friends_list, logged_in_user=logged_in_user, friends_of_user=friends_of_user,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)

@app.route('/course/<course>')
def course_page(course):
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()
    students = doing_course(course)
    user_dict = map_id_to_object(students)

    page_finish()
    return render_template('course.html', course=course, logged_in_user=logged_in_user, students=students, user_dict=user_dict,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)



@app.route('/recommended')
def show_recommended():
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()
    recommended = find_common_courses(session.get("loggedInUser"))
    user_dict = map_id_to_object(recommended)

    page_finish()
    return render_template('recommended.html', logged_in_user=logged_in_user, recommended=recommended, user_dict=user_dict,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)

def map_id_to_object(map):
    dict = {}
    for key in map:
        dict[key] = find_by_id(key)
    return dict


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(url_for('user', username=logged_in_user.username))

        file = request.files['file']
        if file:
            filename = logged_in_user.username + ".png"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            update_img_path(logged_in_user.username)
        return redirect(url_for('user', username=logged_in_user.username))

    friends_of_user = [profile.user_id for profile in friends_by_id(session.get("loggedInUser"))]
    pending_friends_of_user = [profile.user_id for profile in pending_friends_by_id(session.get("loggedInUser"))]

    for profile in pending_friends_of_user:
        print(profile)

    user = find_by_username(username)
    if user is not None:
        courses = timetable_by_username(username)
        busy_times = get_busy_times(courses)

    page_finish()
    if user is None:
        return page_not_found(404)
    all_courses_list = all_courses()
    return render_template('user.html', logged_in_user=logged_in_user, user=user, friends_of_user=friends_of_user, privacy_fn=utilities.profile.is_private,
                           courses=courses, busy_times=busy_times, notifications=notifications, sender_dict=sender_dict, friends_notifications=friends_notifications,
                           receiver_dict=receiver_dict, all_courses=all_courses_list, pending_friends_of_user=pending_friends_of_user, time=time.time())


@app.route('/removeFriend/<username>', methods=['GET'])
def remove_friend(username):
    page_init_lite()

    logged_in_user = find_by_id(session.get("loggedInUser"))

    friends_of_user = [profile.user_id for profile in friends_by_id(session.get("loggedInUser"))]
    user = find_by_username(username)
    remove_friend_from_db(logged_in_user.user_id, user.user_id)

    page_finish()
    return redirect(url_for('user', username=user.username))


@app.route('/cancelFriendRequest/<username>', methods=['GET'])
def cancel_friend_request(username):
    page_init_lite()

    logged_in_user = find_by_id(session.get("loggedInUser"))

    user = find_by_username(username)
    remove_friend_request_from_db(logged_in_user.user_id, user.user_id)

    page_finish()
    return redirect(url_for('user', username=user.username))

@app.route("/class/create", methods=['POST'])
def class_create():
    page_init_lite()

    user_id = str(session.get("loggedInUser"))
    selection = request.form["course"]
    course_name, class_id = selection.split()

    selected_courses = courses_on_code_and_id(course_name, class_id)
    for course in selected_courses:
        add_class(user_id, course['course_code'], course['start_time'], course['day'], course['length'],
                           course['activity'])

    logged_in_user = find_by_id(session.get("loggedInUser"))
    logged_in_user.last_update = -1
    logged_in_user = utilities.profile.update_statuses([logged_in_user])[0]
    page_finish()
    return redirect(url_for('user', username=logged_in_user.username))

@app.route('/class/delete/<class_id>')
def class_delete(class_id):
    page_init_lite()
    delete_class(class_id)
    logged_in_user = find_by_id(session.get("loggedInUser"))
    logged_in_user.last_update = -1
    logged_in_user = utilities.profile.update_statuses([logged_in_user])[0]
    page_finish()
    return redirect(url_for('user', username=logged_in_user.username))

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()

    error_message = ''
    if request.method == 'POST':
        old_pw = request.form.get('input-old-password')
        if old_pw == logged_in_user.password:
            new_username = request.form.get('input-username')
            if not utilities.profile.change_username(logged_in_user, new_username):
                error_message += 'Username already taken.'
            new_password = request.form.get('input-new-password')
            if new_password not in ['', ' ']:
                utilities.profile.change_password(logged_in_user, new_password)
            new_email = request.form.get('input-email')
            if not utilities.profile.change_email(logged_in_user, new_email):
                error_message += ('\nEmail already taken.' if error_message else 'Email already taken.')
            new_status = request.form.get('input-status')
            set_auto = None
            if new_status == 'Automatic':
                set_auto = True
                logged_in_user = utilities.profile.update_statuses([logged_in_user])[0]
            else:
                set_auto = False
                logged_in_user.last_update = -1
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
            # privacy settings stuff
            p_email = True if request.form.get('privacy-email') else False
            p_dob = True if request.form.get('privacy-dob') else False
            p_gender = True if request.form.get('privacy-gender') else False
            p_degree = True if request.form.get('privacy-degree') else False
            print(p_email, p_dob, p_gender, p_degree, set_auto)
            utilities.profile.set_flags(logged_in_user, email=p_email, dob=p_dob, gender=p_gender, degree=p_degree, auto=set_auto)

        else:
            error_message = 'Incorrect password.'

    page_finish()
    return render_template('settings.html', logged_in_user=logged_in_user, statuses=utilities.profile.statuses, utils=utilities.profile,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict, error_message=error_message)


@app.route("/search", methods=['GET'])
def user_search():
    logged_in_user, notifications, friends_notifications, sender_dict, receiver_dict = page_init()

    # get arguments
    search_query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)
    # set how many results per page
    per_page = 10

    profiles = []
    # if query exists
    if search_query:
        results = search_users(search_query)
        profiles = [
            { 'first_name': p['firstname'],
              'last_name': p['lastname'],
              'username': p['username'],
              'imgpath': p['imgpath'],
              'user_id': p['id']
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

    page_finish()
    return render_template('search.html', logged_in_user=logged_in_user, search=search_query, results=users, page=page, count=len(profiles), page_count=page_count,
                           notifications=notifications, friends_notifications=friends_notifications, sender_dict=sender_dict, receiver_dict=receiver_dict)


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

    return redirect(redirect_url())

@app.route('/acceptFriendRequest', methods=['POST','GET'])
def accept_friend_request():
    to_user_id = session.get("loggedInUser")
    from_user_id = request.args.get("userId")
    accept_friend_request_db(from_user_id, to_user_id)
    return redirect(redirect_url())

@app.route('/rejectFriendRequest', methods=['POST', 'GET'])
def reject_friend_request():
    to_user_id = session.get("loggedInUser")
    from_user_id = request.args.get("userId")
    reject_friend_request_db(from_user_id, to_user_id)
    return redirect(redirect_url())

@app.route('/deleteFriendRequest', methods=['POST', 'GET'])
def delete_friend_request():
    from_user_id = session.get("loggedInUser")
    to_user_id = request.args.get("userId")
    delete_friend_request_db(from_user_id, to_user_id)
    return redirect(redirect_url())

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

    return redirect(redirect_url())


@app.route('/acceptMeetUpRequest', methods=['POST','GET'])
def accept_meetup_request():
    id = request.args.get("id")
    to_user_id = session.get("loggedInUser")
    from_user_id = request.args.get("userId")
    accept_request(id, from_user_id, to_user_id)
    return redirect(redirect_url())


@app.route('/rejectMeetUpRequest', methods=['POST', 'GET'])
def reject_meetup_request():
    id = request.args.get("id")
    reject_request(id)
    return redirect(redirect_url())


@app.route('/deleteMeetUpRequest', methods=['POST', 'GET'])
def delete_meetup_request():
    id = request.args.get("id")
    delete_request(id)
    return redirect(redirect_url())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)


if __name__ == '__main__':
    app.run(debug=True)
