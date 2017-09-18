from flask import Flask, request, render_template
from dao.UserProfileDao import*

app = Flask(__name__)

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
    return render_template("signin.html", available=available)

@app.route("/login", methods=['POST'])
def login():
    username = request.form["inputEmail"]
    password = request.form["inputPassword"]
    profile = findByEmailAndPass(username, password)
    if (profile != None):
        return render_template("home.html", loggedInUser=profile)
    else:
        return render_template("signin.html", errorMessage="Incorrect username or password")


if __name__ == "__main__":
    app.run(debug=True)
