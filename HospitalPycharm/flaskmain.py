from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
staff = []
patients = []


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
    patients.append(
        {"first": request.args.get("fname"), "last": request.args.get("lname"), "severity": request.args.get("sevr")})
    print("added")
    print(request.args.get("fname"))
    print(request.args.get("lname"))
    print(request.args.get("sevr"))
    return redirect("/")


@app.route("/list_patients")
def list_patients():
    return render_template("list_patients.html", patients=patients)


@app.route("/form_add_staff")
def form_add_staff():
    return render_template("form_add_staff.html")


@app.route("/add_staff")
def add_staff():
    staff.append({"first": request.args.get("fname"), "last": request.args.get("lname")})
    print("added")
    print(request.args.get("fname"))
    print(request.args.get("lname"))
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
        else:
            return "notokay"
    return "bad"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
