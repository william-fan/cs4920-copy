from flask import Flask, render_template, url_for, redirect, request, session
from services.UserProfileService import*
import status

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
    logged_in_user = find_by_id(session.get("loggedInUser"))
    # TODO: get list of logged-in user's friends that are available
    available = [
        {
            'first_name': 'Cheston',
            'last_name': 'Lee',
            'userid': 'chestonlee'
        },
        {
            'first_name': 'David',
            'last_name': 'Bassin',
            'userid': 'davidbassin'
        },
        {
            'first_name': 'William',
            'last_name': 'Fan',
            'userid': 'williamfan'
        },
        {
            'first_name': 'Darren',
            'last_name': 'Zhu',
            'userid': 'darrenzhu'
        },
    ]
    return render_template('available.html', available=available)

@app.route('/todo')
def todo():
    logged_in_user = find_by_id(session.get("loggedInUser"))
    # TODO: get logged-in user's todo list
    tasks = [
        {
            'name': 'Presentation',
            'subject': 'COMP4920',
            'date': 'Monday 11 September'
        },
        {
            'name': 'Document',
            'subject': 'COMP4920',
            'date': 'Sunday 17 September'
        },
        {
            'name': 'Report',
            'subject': 'COMP4920',
            'date': 'Monday 2 October'
        },
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
