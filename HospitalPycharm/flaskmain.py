from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = []
doctors = []
nurses = []

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/index")
def index():
    return redirect("/")

@app.route("/addingpatient")
def addingpatient():
    return render_template("addingpatient.html")


@app.route("/addpatient")
def addpatient():
    users.append({"first": request.args.get("fname"), "second": request.args.get("lname"), "third": request.args.get("sevr")})
    print("added")
    print(request.args.get("fname"))
    print(request.args.get("lname"))
    print(request.args.get("sevr"))
    return redirect("/")


@app.route("/accesspatients")
def accesspatients():
    return render_template("accesspatients.html", users=users)

@app.route("/addingdoctor")
def addingdoctor():
    return render_template("addingdoctor.html")


@app.route("/adddoctor")
def adddoctor():
    doctors.append({"first": request.args.get("fname"), "second": request.args.get("lname")})
    print("added")
    print(request.args.get("fname"))
    print(request.args.get("lname"))
    return redirect("/")


@app.route("/accessdoctors")
def accessdoctors():
    return render_template("accessdoctors.html", doctors=doctors)

@app.route("/addingnurse")
def addingnurse():
    return render_template("addingnurse.html")


@app.route("/addnurse")
def addnurse():
    nurses.append({"first": request.args.get("fname"), "second": request.args.get("lname")})
    print("added")
    print(request.args.get("fname"))
    print(request.args.get("lname"))
    return redirect("/")

@app.route("/accessnurses")
def accessnurses():
    return render_template("accessnurses.html", nurses=nurses)





if __name__ == "__main__":
    app.run()
