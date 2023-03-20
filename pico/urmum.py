from flask import Flask, make_response
import requests

app = Flask(__name__)

def generateMetrics():
    return "hello world"
    

@app.route('/')
def hello_world():
    response = make_response(generateMetrics(), 200)
    response.mimetype = "text/plain"
    return response

if __name__ == '__main__':
    app.run(port=3000)
