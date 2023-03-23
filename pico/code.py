import time
import usb_cdc
import json
import time, sys, supervisor
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#usb_cdc.enable(console=True, data=True)

if usb_cdc.data is None:
    print("Need to enable USB CDC serial data in boot.py!")
    while True:
        pass


def read_data():
    #usbl = usb_cdc.data.readline()
    n = supervisor.runtime.serial_bytes_available
    s = sys.stdin.read(n)  # actually read it in
    if s == "A":
        led.value = True;
        print(s)
        time.sleep(1)
        led.value = False
        usb_cdc.data.write("Response Received")


    #print(input() + "posdfopsdf")

    # print both text & hex version of recv'd chars (see control chars!)
    #print("got:", " ".join("{:s} {:02x}".format(c,ord(c)) for c in s))
    #print( data)
    #data = {"raw": usbl.decode()}
    #data = usbl.decode()

usb_cdc.data.timeout = 5

while True:
    read_data()
    time.sleep(1)
