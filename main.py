import time
from flask import Flask, render_template, url_for, redirect, request, session
from services.UserProfileService import*
import status

from flask import Flask, render_template, url_for
from classes.ToDo import ToDo
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
          'userid': p.user_id,
          'imgpath': p.imgpath
        } for p in friends_of_user
        if p.status == status.statuses[0]
    ]
    return render_template('available.html', available=available)

@app.route('/todo')
def todo():
    logged_in_user = find_by_id(session.get("loggedInUser"))
    # TODO: get logged-in user's todo list
    todo_list = load_todos(session.get("loggedInUser"))
    tasks = []
    for task in todo_list:
        tasks += [
            {
                'name': task['title'],
                'text': task['description'],
                'subject': task['course_name'],
                'date': task['end_time']
            }
        ]

    return render_template('todo.html', tasks=tasks)


@app.route('/todo/createpage')
def todo_createpage():
    logged_in_user = find_by_id(session.get("loggedInUser"))
    # TODO: get logged-in user's todo list
    return render_template('todocreate.html')


@app.route("/todo/create", methods=['POST'])
def todo_create():
    add_todo("a", request.form["title"], request.form["description"], str(session.get("loggedInUser")), request.form["course"], str(time.time()), request.form["date"])
    todo_list = load_todos(session.get("loggedInUser"))
    tasks = []
    for task in todo_list:
        tasks += [
            {
                'name': task['title'],
                'text': task['description'],
                'subject': task['course_name'],
                'date': task['end_time']
            }
        ]
    return render_template('todo.html', tasks=tasks)


def get_busy_times(courses):
    busy_times = []
    for course in courses:
        for i in range(course['length']):
            busy_times.append({'day': course['day'], 'time': course['time']+i})
    return busy_times

@app.route('/user/<userid>')
def user(userid):
    # TEMPORARY
    logged_in_user = find_by_id(session.get("loggedInUser"))
    # TODO: get profile page user's details
    user = {
        'first_name': logged_in_user.first_name,
        'last_name': logged_in_user.last_name,
        'userid': userid,
        'status': logged_in_user.status,
        'email': logged_in_user.email,
        'degree': 'Computer Science'
    }


    # TODO: get profile page user's courses
    courses = [
        {
            'day': 2,
            'time': 12,
            'length': 2,
            'subject': 'COMP4920',
            'activity': 'Lecture'
        },
        {
            'day': 0,
            'time': 12,
            'length': 2,
            'subject': 'COMP4920',
            'activity': 'Seminar'
        },
        {
            'day': 0,
            'time': 18,
            'length': 3,
            'subject': 'COMP9444',
            'activity': 'Lecture'
        },
        {
            'day': 2,
            'time': 15,
            'length': 3,
            'subject': 'COMP4418',
            'activity': 'Lecture'
        },
    ]

    busy_times = get_busy_times(courses)


    return render_template('user.html', user=user, courses=courses, busy_times=busy_times)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        new_status = request.form.get('input_status')
        logged_in_user = find_by_id(session.get("loggedInUser"))
        status.change_status(logged_in_user, new_status)
    return render_template('settings.html', statuses=status.statuses)


@app.errorhandler(404)
def page_not_found(e):
    return '404 <button onclick="window.history.back()">Go Back</button>', 404

if __name__ == '__main__':
    app.run(debug=True)
