from flask import Flask, render_template, request, jsonify
from flask_cors import CORS


app = Flask(__name__)


CORS(app, resources={r"/*": {"origins": "http://cpen291-2.ece.ubc.ca/"}})


@app.route("/start")
def homepage():
    return render_template("startPage.html")

@app.route("/")
def homepage2():
    return render_template("startPage.html")

@app.route("/game")
def gamepage():
    return render_template("gamePage.html")


@app.route('/', methods=['GET'])
def handle_request():
    data = request.get_json()
    # Process the data as needed
    response_data = {'message': 'Received request', 'data': data}
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host = "5000", debug=True)
    print(handle_request())


