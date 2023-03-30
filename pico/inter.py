from flask import Flask, make_response, jsonify, request
import requests
from flask_cors import CORS
import json
import serial
import time
import re

# sends json requests to the server/VM from own computer internet port
app = Flask(__name__)
CORS(app)


def  displayText():
    return "hello world"

#serial port for Ardi's Macbook Pro
ser = serial.Serial('/dev/cu.usbmodem101') # open serial port


#send data through the serial connection
def sendData(data):
    send = data + "\r"
    ser.write(send.encode('utf8'))



def readData():
    s = ser.readline()
    k = s.decode('utf8')
    return " ".join(k.split())

#sends data to the server from pico
@app.route('/')
def hello_world():
    response = make_response(displayText(), 200)
    response.mimetype = "text/plain"
    print(readData())
    response = {"test": readData()}
    global ser
    #misc code heres
    time.sleep(0.1)
    return jsonify(response)

##Gets post request made by the server
@app.route('/', methods = ['POST'])
def receivepost():
    data = request.get_json()
    sendData(json.dumps(data))
    return data




if __name__ == '__main__':
    app.run(port=3000)
