import serial
import time
import requests
import json

ser = serial.Serial('/dev/cu.usbmodem101') # open serial port




def sendData(data):
    send = data + " \r\n"
    ser.write(send.encode('utf8'))

def main():
    global ser
    while 1:
        #misc code here
        sendData("B")
        time.sleep(0.4)
        print(1)


url = "http://cpen291-2.ece.ubc.ca/"
data = {"key": "value"}

# while True:
#     response = requests.post(url, data=data)
#     print(response.text)
#     time.sleep(2)



if __name__ == "__main__":
    main()
