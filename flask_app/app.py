from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json

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

@app.route("/end")
def endpage():
    return render_template("endPage.html")



# @app.route("/hole", methods=['POST'])
# def hole():
#     data = request.get_json()
#     print(data)
#     return jsonify(data)


@app.route('/hole1', methods=['POST'])
def handle_request():
    data = request.data.decode('utf-8')  # decode the data from bytes to string
    print(data)  # print the data string to console
    return jsonify(data)
# response_data = {'data': data}
    # print(response_data)
    # return jsonify(response_data)


if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)


