from flask import Flask, make_response, jsonify, request
import requests
from flask_cors import CORS
import json
import serial
import time
import re
import threading
from multiprocessing import Process
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


def parallelize_functions(*functions):
    processes = []
    for function in functions:
        p = Process(target=function)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    def readline(self):
        i = self.buf.find(b"\n")
        if i >= 0:
            r = self.buf[:i+1]
            self.buf = self.buf[i+1:]
            return r
        while True:
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            i = data.find(b"\n")
            if i >= 0:
                r = self.buf + data[:i+1]
                self.buf[0:] = data[i+1:]
                return r
            else:
                self.buf.extend(data)

rl = ReadLine(ser)


def picoData():
    while True:
        send = rl.readline().decode('utf8')
        print(send)
        if "One\r\n" in send:
            send_post_request("One True")
        if "Two\r\n" in send:
            send_post_request("Two True")
        if "Three\r\n" in send:
            send_post_request("Three True")
        if "Four\r\n" in send:
            send_post_request("Four True")
        if "Five\r\n" in send:
            send_post_request("Five True")
        if "Six\r\n" in send:
            send_post_request("Six True")

        time.sleep(0.01)


##Gets post request made by the server
@app.route('/', methods = ['POST'])
def receivepost():
    data = request.get_json()
    sendData(json.dumps(data))
    return data






def send_post_request(data):
    url = 'http://cpen291-2.ece.ubc.ca/hole1' # replace with the URL of the endpoint you want to send the request to
    headers = {'Content-Type': 'application/json'}
    print(data)
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response)
    if response.status_code == 200:
        print("POST request sent successfully!")
    else:
        print("Error sending POST request: ", response.status_code)






def run_app():
    app.run(port=3000, debug=False)

if __name__ == '__main__':
    parallelize_functions(picoData, run_app)

