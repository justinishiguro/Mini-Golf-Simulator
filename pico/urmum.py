from flask import Flask, make_response, jsonify, request
import requests
from flask_cors import CORS
import json
import serial
import time


# sends json requests to the server/VM from own computer internet port
app = Flask(__name__)


CORS(app)


def  displayText():
    return "hello world"


ser = serial.Serial('/dev/cu.usbmodem101') # open serial port



#send data through the serial connection
def sendData(data):
    print("TEsting")
    send = data + "\r"
    ser.write(send.encode('utf8'))



#sends data to the server
@app.route('/')
def hello_world():
    response = make_response(displayText(), 200)
    response.mimetype = "text/plain"
    response = {"test": "hi"}
    print(response)
    global ser
    #misc code heres
    time.sleep(0.1)
    print(1)

    return jsonify(response)


@app.route('/', methods = ['POST']) #receiving post request
def receivepost():
    data = request.get_json()
    converted = str()

    for key in data:
        converted += key + str(data[key]) + "."
    print(converted)

    sendData(json.dumps(data))
    return data









if __name__ == '__main__':
    app.run(port=3000)
