from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)
staff = []
patients = []

def compare(x,y):
    return x["priority"] > y["priority"]

def sortQueue():
    patients.sort(key=lambda x: x["severity"])

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/index")
def index():
    return redirect("/")


@app.route("/form_add_patient")
def form_add_patient():
    return render_template("form_add_patient.html")


@app.route("/add_patient")
def add_patient():
    new = {
        "first": request.args.get("fname"),
        "last": request.args.get("lname"),
        "severity": request.args.get("sevr"),
        "time": time.time()
    }
    patients.append(new)
    print(new)
    sortQueue()
    return redirect("/")


@app.route("/list_patients")
def list_patients():
    return render_template("list_patients.html", patients=patients)


@app.route("/form_add_staff")
def form_add_staff():
    return render_template("form_add_staff.html")


@app.route("/add_staff")
def add_staff():
    fname = request.args.get("fname")
    lname = request.args.get("lname")
    new = {
        "first": fname,
        "last": lname,
        "type": request.args.get("type"),
        "username":
            (fname[:3] if len(fname) > 3 else fname)
            + (lname[:3] if len(lname) > 3 else lname)
            + str(sum(ord(a) for a in (fname+lname)) % 100),
        "password": request.args.get("pass")
    }
    staff.append(new)
    sortQueue()
    print(new)
    return redirect("/")


@app.route("/list_staff")
def list_staff():
    return render_template("list_staff.html", staff=staff)


@app.route("/login")
def login():
    print(request.args)
    username = request.args.get("username")
    password = request.args.get("password")
    for user in staff:
        if user["username"] == username and user["password"] == password:
            return "okay"
    return "bad"



if __name__ == "__main__":
    app.run(host="0.0.0.0")
