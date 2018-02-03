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

if __name__ == "__main__":
    app.run()
