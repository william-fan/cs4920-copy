import time
from flask import Flask, render_template, url_for, redirect, request, session
from services.UserProfileService import *
import status

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
    friends_of_user = friends_by_id(session.get("loggedInUser"))
    available = [
        { 'first_name': p.first_name,
          'last_name': p.last_name,
          'username': p.username,
          'imgpath': p.imgpath
        } for p in friends_of_user
        if p.status == status.statuses[0]
    ]


    logged_in_user = get_username_from_user_id(session.get("loggedInUser"))
    return render_template('available.html', logged_in_user=logged_in_user, available=available)


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

    logged_in_user = get_username_from_user_id(session.get("loggedInUser"))
    return render_template('todo.html', logged_in_user=logged_in_user, tasks=tasks)

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


@app.route('/user/<username>')
def user(username):
    user = find_by_username(username)

    courses = timetable_by_username(username)

    busy_times = get_busy_times(courses)


    logged_in_user = get_username_from_user_id(session.get("loggedInUser"))
    return render_template('user.html', logged_in_user=logged_in_user, user=user, courses=courses, busy_times=busy_times)


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
    if request.method == 'POST':
        new_status = request.form.get('input_status')
        logged_in_user = find_by_id(session.get("loggedInUser"))
        status.change_status(logged_in_user, new_status)

    logged_in_user = get_username_from_user_id(session.get("loggedInUser"))
    return render_template('settings.html', logged_in_user=logged_in_user, statuses=status.statuses)


@app.route("/search", methods=['GET'])
def user_search():
    search_query = request.args.get('q')
    results = search_users(search_query)
    profiles = [
        { 'first_name': p['firstname'],
          'last_name': p['lastname'],
          'username': p['username'],
          'imgpath': p['imgpath']
        } for p in results
    ]
    logged_in_user = get_username_from_user_id(session.get("loggedInUser"))
    return render_template('search.html', logged_in_user=logged_in_user, results=profiles)


@app.errorhandler(404)
def page_not_found(e):
    return '404 <button onclick="window.history.back()">Go Back</button>', 404


if __name__ == '__main__':
    app.run(debug=True)
