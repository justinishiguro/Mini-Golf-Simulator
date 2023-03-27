import time
import usb_cdc
import json
import time, sys, supervisor
import board
import digitalio
import re
import busio
from adafruit_motor import servo
import pwmio


elbow = servo.Servo(pwmio.PWMOut(board.GP15, duty_cycle = 2 ** 15 , frequency=50))


pwm = pwmio.PWMOut(board.GP16, frequency=50)
my_servo = servo.ContinuousServo(pwm)


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#usb_cdc.enable(console=True, data=True)
# set the pulse duration range for backward rotatio





if usb_cdc.data is None:
    print("Need to enable USB CDC serial data in boot.py!")
    while True:
        pass


def read_data():
    #usbl = usb_cdc.data.readline()
    n = supervisor.runtime.serial_bytes_available
    s = sys.stdin.readline()  # actually read it in
    #writes back to the terminal


   # print(int(re.search(r'"Height": 5', s)))
    new = []
    j = ""
    for x in s:
        if x.isdigit():
            j+=x
    elbow.angle = (int(j))*4


   #print(re.findall(r'\d+',s))




usb_cdc.data.timeout = 5

while True:
    read_data()
    time.sleep(0.1)


