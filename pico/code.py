import time, sys, supervisor
import board
import digitalio
import re
import busio
from adafruit_motor import servo
import pwmio
import usb_cdc


elbow = servo.Servo(pwmio.PWMOut(board.GP15, duty_cycle = 2 ** 15 , frequency=50))

base = servo.Servo(pwmio.PWMOut(board.GP14, duty_cycle = 2 ** 15 , frequency=50))


club = servo.Servo(pwmio.PWMOut(board.GP12, duty_cycle = 2 ** 15 , frequency=50))


pwm = pwmio.PWMOut(board.GP16, frequency=50)
rotator = servo.ContinuousServo(pwm)


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT




holes = [False, False, False, False, False]


score = holes.count(True)




if usb_cdc.data is None:
    print("Need to enable USB CDC serial data in boot.py!")
    while True:
        pass


def read_example():
    #usbl = usb_cdc.data.readline()
    n = supervisor.runtime.serial_bytes_available
    s = sys.stdin.readline()  # actually read it in
    #writes back to the terminal

    j = ""
    for x in s:
        if x.isdigit():
            j+=x
    elbow.angle = (int(j))*4


def read_power(power):
    j= ''
    for x in s:
        if x.isdigit():
            j+=x
    if int(j) < 117:
        elbow.angle = (int(j))*4
    print(elbow.angle)


def read_height(height):
    j= ''
    for x in s:
        if x.isdigit():
            j+=x
    if int(j) < 117:
        elbow.angle = (int(j))*4
    print(elbow.angle)



def read_rotation(rotation):
    print(rotation)



def read_throttle(throttle):
    print(throttle)



#Keeps track of the users score and how many holes they have gotten in
def scoreTracker():
    i = 0
    #writes back to the terminal


#Notifiy the web app if the user has won the game
def isWin():
    #usbl = usb_cdc.data.readline()
    n = supervisor.runtime.serial_bytes_available
    s = sys.stdin.readline()  # actually read it in
    #writes back to the terminal


#To check if the hit button was pressed
def hit(state):
    #usbl = usb_cdc.data.readline()
    n = supervisor.runtime.serial_bytes_available
    s = sys.stdin.readline()  # actually read it in

    if score == 6:
        print('WIN')



usb_cdc.data.timeout = 5

while True:
    #get the serial text
    n = supervisor.runtime.serial_bytes_available
    s = sys.stdin.readline()  # actually read it in
    #determine what was sent by parsing the string
    if "Height" in s:
        read_height(s)



    time.sleep(0.05)

