from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/available')
def available():
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
    # TODO: get profile page user's details
    user = {
        'first_name': 'Jordan',
        'last_name': 'Cohn',
        'status': 'Available',
        'email': 'jordan.cohn@student.unsw.edu.au',
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

@app.route('/signout')
def signout():
    return 'Signed out'


@app.errorhandler(404)
def page_not_found(e):
    return '404 <button onclick="window.history.back()">Go Back</button>', 404

if __name__ == '__main__':
    app.run(debug=True)
