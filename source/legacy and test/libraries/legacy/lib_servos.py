from servo import *

servo = Servo()

angle = 120

servo.set_servo_pwm("0", angle)
servo.set_servo_pwm("1", angle)
