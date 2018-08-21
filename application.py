import os

from flask import Flask, session, render_template, request
from flask_session import Session
from models import *

app = Flask(__name__)
db.init_app(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['FLASK_DEBUG'] = 1
Session(app)


@app.route("/")
def index():
    return "Я почав це робити :)"


@app.route("/reg")
def reg():
    return render_template('reg.html')


@app.route("/login", methods=['GET', 'POST'])
def log():
    if request.method != "POST":
        return render_template("login.html")
    else:
        name = request.form['name']
        password = request.form['password']
        print(name, password)
        user = Users.query.filter_by(name=name)
        # if user.password == password:
        #     # user logged
        #     pass
        # else:
        return render_template("login.html", message= "wrong name/password")
