from servo import *
from ultrasonic import *
import time

servo = Servo()
dist_sensor = Ultrasonic()
objectPresent = False
baseHorizontalAngle = 90
baseVerticalAngle = 80
servo.set_servo_pwm("1", baseVerticalAngle) #1 = up and down
servo.set_servo_pwm("0", baseHorizontalAngle) #0 = left and right

def sweepSides():
    dist = dist_sensor.get_distance()
    leftSide = False
    rightSide = False
    servo.set_servo_pwm("1", 80)
    servo.set_servo_pwm("0", 10)
    dist = dist_sensor.get_distance()
    if dist <= 5:
        leftSide = True
    time.sleep(2)
    servo.set_servo_pwm("0", 170)
    dist = dist_sensor.get_distance()
    if dist <= 5:
        rightSide = True
    print(f"left side = {leftSide}")
    print(f"right side = {rightSide}")
    time.sleep(2)
    servo.set_servo_pwm("1", baseVerticalAngle)
    servo.set_servo_pwm("0", baseHorizontalAngle)

while True:
    dist = dist_sensor.get_distance()
    print(f"Current distance is {dist} cm")
    if dist <= 5:
        objectPresent = True
        print(objectPresent)
        sweepSides()
    else:
        objectPresent = False
        print(objectPresent)
    time.sleep(0.5)
