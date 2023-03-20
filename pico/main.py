import serial
import time

ser = serial.Serial('/dev/cu.usbmodem142201') # open serial port
def sendData(data):
    send = data + " \r\n"
    ser.write(send.encode('utf8'))

def main():
    global ser
    while 1:
        #misc code here
        sendData("A")
        print("1")
        time.sleep(1)
        print("2")




if __name__ == "__main__":
    main()
