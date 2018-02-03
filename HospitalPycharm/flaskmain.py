from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/yeet")
def yeet():
    print("okay")
    return "kk"

if __name__ == "__main__":
    app.run()
