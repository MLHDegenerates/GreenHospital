from flask import Flask, render_template, request, redirect, url_for
import time
import os
import operator
import json

app = Flask(__name__)
staff = []
patients = []
messages = []

if os.path.exists("users.txt"):
    file = open("users.txt", "r")
    for line in file:
        data = line.split(" ")
        if len(data) == 5:
            patients.append({
                "first": data[0],
                "last": data[1],
                "severity": data[2],
                "time": data[3]
            })
        elif len(data) == 6:
            staff.append({
                "first": data[0],
                "last": data[1],
                "type": data[2],
                "username": data[3],
                "password": data[4]
            })
    file.close()


def writetofile():
    file = open("users.txt", "w")
    for pat in patients:
        for i, v in pat.items():
            file.write(str(v) + " ")
        file.write("\n")
    for doc in staff:
        for i, v in doc.items():
            file.write(str(v) + " ")
        file.write("\n")
    file.close()



@app.route("/")
def hello():
    return render_template("index.html", staff=staff)


@app.route("/index")
def index():
    return redirect("/")


@app.route("/form_add_patient")
def form_add_patient():
    return render_template("form_add_patient.html")



def sortQueue(patients):

    patients.sort(key=operator.itemgetter('severity'))
    return patients

@app.route("/add_patient")
def add_patient():
    new = {
        "first": request.args.get("fname"),
        "last": request.args.get("lname"),
        "severity": request.args.get("sevr"),
        "time": int(time.time())
    }
    patients.append(new)
    print(new)
    writetofile()
    sortQueue(patients)
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
            + str(sum(ord(a) for a in (fname + lname)) % 100),
        "password": request.args.get("pass")
    }
    staff.append(new)
    writetofile()
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
            return user["username"]
    return "<Bad Login>"

@app.route("/fetchmsg")
def fetchmsg():
    if len(messages) == 0:
        return "[]"
    print(request.args)
    lastfetch = int(request.args.get("time"))
    send = [a for a in messages if a["time"] > lastfetch and (a["receiver"] == request.args.get("receiver") or a["sender"] == request.args.get("receiver"))]
    return json.dumps({"last": messages[-1]["time"], "messages": send})

@app.route("/sendmsg")
def sendmsg():
    messages.append({
        "message": request.args.get("message"),
        "time": int(time.time()),
        "receiver": request.args.get("receiver"),
        "sender": request.args.get("sender")
    })
    return "ok"

@app.route("/compose")
def compose():
    return render_template("compose.html", staff=staff)

if __name__ == "__main__":
    print("http://127.0.0.1:5000")
    app.run(host="0.0.0.0")

