from flask import Flask, request, render_template, session
from services.UserProfileService import*

app = Flask(__name__)
app.secret_key = "secret-key"

available = [
    {
        "name": "Jordan"
    },
    {
        "name": "Cheston"
    },
    {
        "name": "William"
    },
    {
        "name": "David"
    },
    {
        "name": "Darren"
    }
]

@app.route("/")
def index():
    if (session.get("loggedInUser") is not None):
        return render_template("home.html", loggedInUser=find_by_id(session.get("loggedInUser")))
    else:
        return render_template("signin.html")

@app.route("/login", methods=['POST'])
def login():
    username = request.form["inputEmail"]
    password = request.form["inputPassword"]
    profile = find_by_email_pass(username, password)
    if (profile is not None):
        session['loggedInUser'] = profile.id
        return render_template("home.html", loggedInUser=profile)
    else:
        return render_template("signin.html", errorMessage="Incorrect username or password")

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
        return render_template("register.html", registerError=", ".join(errors))

    register_user(username, password, email, firstname, lastname, gender, dob)
    return render_template("created.html")

@app.route("/registerPage")
def displaySignIn():
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
