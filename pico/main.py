import serial
import time

ser = serial.Serial('/dev/cu.usbmodem142201') # open serial port
def sendData(data):
    data += "\r\n"
    ser.write(data.encode())


def main():
    global ser
    while 1:
        #misc code here
        sendData("Hellllllloow")
        print("1")
        time.sleep(1)
        print("2")

        time.sleep(1)
        print("3")

        time.sleep(1)
        print("4")

        time.sleep(1)
        print("5")



if __name__ == "__main__":
    main()
