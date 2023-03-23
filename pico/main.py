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
        sendData("A")
        time.sleep(0.4)
        print(1)




if __name__ == "__main__":
    main()
