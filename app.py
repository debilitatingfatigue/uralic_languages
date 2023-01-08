from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/main")
def index():
    return render_template("main.html")


@app.route("/grades")
def grades():
    return render_template("grades.html")


@app.route("/presentations")
def presentations():
    return render_template("presentations.html")


@app.route("/homeworks")
def homeworks():
    return render_template("homeworks.html")

if __name__ == "__main__":
    app.run()