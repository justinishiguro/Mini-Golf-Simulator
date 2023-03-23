from flask import Flask, make_response, jsonify
import requests
from flask_cors import CORS
import json



# sends json requests to the server/VM from own computer internet port

app = Flask(__name__)


CORS(app)


def generateMetrics():
    return "hello world"


@app.route('/')
def hello_world():
    response = make_response(generateMetrics(), 200)
    response.mimetype = "text/plain"
    response = {"test": "hi"}
    print(response)
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3000)
