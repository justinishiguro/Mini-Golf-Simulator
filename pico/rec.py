import requests
import json
import serial
import time
import re


#serial port for Ardi's Macbook Pro
ser = serial.Serial('/dev/cu.usbmodem101') # open serial port



def readData():
    try:
        s = ser.readline()
        k = s.decode('utf8')
        return " ".join(k.split())
    except serial.SerialException as e:
        print(f"Error: {e}")
        return None







def send_post_request(data):
    url = 'http://cpen291-2.ece.ubc.ca/' # replace with the URL of the endpoint you want to send the request to
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        print("POST request sent successfully!")
    else:
        print("Error sending POST request: ", response.status_code)


while True:
    time.sleep(1)
    send_post_request(readData())

