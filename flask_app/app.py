from flask import Flask, render_template

app = Flask(__name__)

@app.route("/start")
def homepage():
    return render_template("gamePage.html")

@app.route("/")
def homepage2():
    return render_template("startPage.html")

@app.route("/game")
def gamepage():
    return render_template("gamePage.html")


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)


