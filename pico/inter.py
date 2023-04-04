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

#Serial port to receive and send Data (address given is for Macbook)
ser = serial.Serial('/dev/cu.usbmodem101') # open serial port


#send data through the serial connection
def sendData(data):
    send = data + "\r"
    #encode the data as binary before being sent
    ser.write(send.encode('utf8'))

#This function initializes the multiprocessing funcitions that allows us to run two functions 
# as the sime time in parallel
def parallelize_functions(*functions):
   # create an empty list to hold Process objects
    processes = []

    # loop through a list of functions and spawn a new Process for each function
    for function in functions:
        # create a new Process object for the current function
        p = Process(target=function)
        # start the new process
        p.start()
        # add the new process to the list of processes
        processes.append(p)

    # loop through the list of Process objects and wait for each process to complete
    for p in processes:
        p.join()


#This Class allows us to recieve data from the pico W
# define a class named ReadLine
class ReadLine:
    # define the __init__ method, which is called when a new ReadLine object is created
    def __init__(self, s):
        # create a new bytearray to hold received data
        self.buf = bytearray()
        # store the serial port object in an instance variable
        self.s = s

    # define the readline method, which reads a line of data from the serial port
    def readline(self):
        # find the index of the first newline character in the buffered data, if present
        i = self.buf.find(b"\n")
        if i >= 0: # if a newline character is found in the buffered data
            # extract the data up to and including the newline character
            r = self.buf[:i+1]
            # remove the extracted data from the buffer
            self.buf = self.buf[i+1:]
            # return the extracted data
            return r
        # if a newline character is not found in the buffered data
        while True:
            # read up to 2048 bytes of data from the serial port or the amount of data currently waiting in the input buffer, whichever is smaller
            i = max(1, min(2048, self.s.in_waiting))
            data = self.s.read(i)
            # find the index of the first newline character in the newly received data, if present
            i = data.find(b"\n")
            if i >= 0: # if a newline character is found in the newly received data
                # concatenate the buffered data with the newly received data up to and including the newline character
                r = self.buf + data[:i+1]
                # remove the concatenated data from the buffer
                self.buf[0:] = data[i+1:]
                # return the concatenated data
                return r
            else: # if a newline character is not found in the newly received data
                # append the newly received data to the buffer
                self.buf.extend(data)


rl = ReadLine(ser)

#This Funciton will allow us to use the readline class and read the data from the 
#pico and send post requests to our web server
def picoData():
    while True:
        #decode the serial data that is being sent by the pico
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


##Gets post request made by the server calls send data to send data to the pico
@app.route('/', methods = ['POST'])
def receivepost():
    data = request.get_json()
    sendData(json.dumps(data))
    return data





#Sends post requests to to the webserver, mainly used to send data from the pico to the webserver
def send_post_request(data):
    # specify the URL of the endpoint to send the POST request to
    url = 'http://cpen291-2.ece.ubc.ca/hole1'

    # specify the headers to include in the request
    headers = {'Content-Type': 'application/json'}

    # print the data that will be sent in the request body
    print(data)

    # send a POST request to the specified URL with the specified headers and data
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # print the response object returned by the server
    print(response)

    # check if the response status code indicates success (HTTP 200 OK)
    if response.status_code == 200:
        # if the request was successful, print a success message
        print("POST request sent successfully!")
    else:
        # if the request was not successful, print an error message with the HTTP status code
        print("Error sending POST request: ", response.status_code)






#Funciton to organize the flask app initialization
def run_app():
    app.run(port=3000, debug=False)

if __name__ == '__main__':
    #Calling the parallelize function to allow both tne flask app and the while loop that
    #listens to the pico at the same time
    parallelize_functions(picoData, run_app)

