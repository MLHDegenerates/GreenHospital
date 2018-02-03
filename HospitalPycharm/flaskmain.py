from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = []

@app.route("/")
def hello():
    return render_template("index.html")



@app.route("/addingpatient")
def addingpatient():
    return render_template("addingpatient.html")


@app.route("/addpatient")
def addpatient():
    users.append({"first": request.args.get("fname"), "second": request.args.get("lname")})
    print("added")
    print(request.args.get("fname"))
    print(request.args.get("lname"))
    return redirect("/")


@app.route("/accesspatients")
def accesspatients():
    return render_template("accesspatients.html", users=users)



if __name__ == "__main__":
    app.run()
