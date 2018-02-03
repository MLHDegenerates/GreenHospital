from flask import Flask, render_template, request

app = Flask(__name__)


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
    return"$$$"

@app.route("/addinguser")
def addinguser():
    return render_template("addinguser.html")

@app.route("/adduser")
def adduser():
    print(request.args.get("fname"))
    print(request.args.get("lname"))
    return hello()

if __name__ == "__main__":
    app.run()
