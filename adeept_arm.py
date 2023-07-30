
from adafruit_servokit import ServoKit
import PCF8591 as ADC
import time
import RPi.GPIO as gpio
from datetime import datetime


SERVO0_MIN = 0
SERVO0_MAX = 360
SERVO1_MIN = 0  #RUNS BACKWARDS; THIS IS THE TOP
SERVO1_MAX = 360 # THIS IS THE BOTTOM
SERVO2_MIN = 0
SERVO2_MAX = 360
SERVO3_MIN = 30
SERVO3_MAX = 360

LEFT_CLICK = 17
RIGHT_CLICK = 18
DOUBLE_CLICK_GRACE_TIME = 4

SPEED = 5

SERVO_MAX = [SERVO0_MAX, SERVO1_MAX, SERVO2_MAX, SERVO3_MAX]
SERVO_MIN = [SERVO0_MIN, SERVO1_MIN, SERVO2_MIN, SERVO3_MIN]

kit = ServoKit(channels=16)

def setUp():
    global SERVO0_MAX, SERVO1_MAX, SERVO2_MAX, SERVO3_MAX
    kit.servo[0].actuation_range = SERVO0_MAX
    kit.servo[1].actuation_range = SERVO1_MAX
    kit.servo[2].actuation_range = SERVO2_MAX
    kit.servo[3].actuation_range = SERVO3_MAX
    ADC.setup(0X48)

    gpio.setup(LEFT_CLICK, gpio.IN, pull_up_down = gpio.PUD_UP)
    gpio.setup(RIGHT_CLICK, gpio.IN, pull_up_down = gpio.PUD_UP)

def readLeftJoyStick():
    # down, up, left, right are i = 1, 2, 3, 4
    # joystick in the center is i = 0
    if ADC.read(0) <= 5:
        return 1
    elif ADC.read(0) >= 200: 
        return 2
    elif ADC.read(1) <= 5: 
        return 3
    elif ADC.read(1) >= 200:
        return 4
    return 0

def readRightJoyStick():
    if ADC.read(2) <= 5:
        return 1
    elif ADC.read(2) >= 200: 
        return 2
    elif ADC.read(3) <= 5: 
        return 3
    elif ADC.read(3) >= 200:
        return 4
    return 0

def getClick():
    return (gpio.input(LEFT_CLICK), gpio.input(RIGHT_CLICK))

def rangeOfMotion():
    kit.servo[0].angle = SERVO0_MIN
    time.sleep(1)
    kit.servo[1].angle = SERVO1_MIN
    time.sleep(1)
    kit.servo[2].angle = SERVO2_MIN
    time.sleep(1)
    kit.servo[3].angle = SERVO3_MIN
    time.sleep(5)
    kit.servo[0].angle = SERVO0_MAX
    time.sleep(1)
    kit.servo[1].angle = SERVO1_MAX
    time.sleep(1)
    kit.servo[2].angle = SERVO2_MAX
    time.sleep(1)
    kit.servo[3].angle = SERVO3_MAX
    time.sleep(5)

def centerAll():
    kit.servo[0].angle = (SERVO0_MAX - SERVO0_MIN) / 2
    kit.servo[1].angle = (SERVO1_MAX - SERVO1_MIN) / 2
    kit.servo[2].angle = (SERVO2_MAX - SERVO2_MIN) / 2
    kit.servo[3].angle = (SERVO3_MAX - SERVO3_MIN) / 2

def moveServo( args ):
    _serv = kit.servo[args[1]].angle
    if _serv + args[0] <= SERVO_MAX[args[1]] and _serv + args[0] >= SERVO_MIN[args[1]]:
        kit.servo[args[1]].angle += args[0]

def prepThrow():
    kit.servo[1].angle = 88
    kit.servo[2].angle = 318
    kit.servo[3].angle = 34

def throw():
    kit.servo[1].angle = 196
    kit.servo[2].angle = 80



def main():
    setUp()
    # rangeOfMotion()
    directions = ["home", "down", "up", "left", "right"]

    _left = [(0, 0), ((SPEED * (-1)), 1), (SPEED, 1), (SPEED, 0), ((SPEED * (-1)), 0)]
    _right = [(0, 0), (SPEED, 2), ((SPEED * (-1)), 2), (SPEED, 3), ((SPEED * (-1)), 3)]
    # center all of the servos before beginnning
    centerAll()
    left = -1
    right = -1
    last_double = datetime.now()
    _throw = False
    while True:
        curr_left = readLeftJoyStick()
        curr_right = readRightJoyStick()
        left_click, right_click = getClick()
        if curr_left != 0:
            moveServo(_left[curr_left])
        if curr_right != 0:
            moveServo(_right[curr_right])
        if left_click == 0 and right_click == 0:
            curr = datetime.now()
            if (curr - last_double).total_seconds() > DOUBLE_CLICK_GRACE_TIME:
                if _throw:
                    throw()
                    _throw = False
                else:
                    prepThrow()
                    _throw = True
                last_double = curr
                time.sleep(0.5)

if __name__ == "__main__":
    main()