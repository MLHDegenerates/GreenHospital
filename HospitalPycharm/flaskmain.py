from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = []

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/yeet")
def yeet():
    print("okay")
    print(request.args.get("message"))
    return "kk"


@app.route("/bitconnect")
def bitconnect():
    print("yes")
    return "$$$"


@app.route("/addinguser")
def addinguser():
    return render_template("addinguser.html")


@app.route("/adduser")
def adduser():
    users.append({"first": request.args.get("fname"), "second": request.args.get("lname")})
    print("added")
    print(request.args.get("fname"))
    print(request.args.get("lname"))
    return redirect("/")


@app.route("/accessusers")
def accessusers():
    return render_template("accessusers.html", users=users)

@app.route ("/type_Luotai")
def type_luotai ():
    print ("Luotai")
    return render_template("addinguser.html")

if __name__ == "__main__":
    app.run()
