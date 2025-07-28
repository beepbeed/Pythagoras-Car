from motor import Ordinary_Car
from infrared import Infrared
from servo import *
from ultrasonic import *
from picamera2 import Picamera2
from adc import ADC
import time
import cv2
import numpy as np
import os

# Initialize hardware
drive = Ordinary_Car()
infrared = Infrared()
servo = Servo()
dist_sensor = Ultrasonic()
picam2 = Picamera2()
adc = ADC()

# Camera setup
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("still")
picam2.start()

# Constants
baseHorizontalAngle = 90
baseVerticalAngle = 80
servo.set_servo_pwm("1", baseVerticalAngle)
servo.set_servo_pwm("0", baseHorizontalAngle)

class Movement:
    def forward(self, power, second=None):
        drive.set_motor_model(-power, -power, -power, -power)
        if second is not None:
            time.sleep(second)
            drive.set_motor_model(0, 0, 0, 0)

    def backward(self, power, second=None):
        drive.set_motor_model(power, power, power, power)
        if second is not None:
            time.sleep(second)
            drive.set_motor_model(0, 0, 0, 0)

    def right(self, power, second=None):
        drive.set_motor_model(-power, -power, power, power)
        if second is not None:
            time.sleep(second)
            drive.set_motor_model(0, 0, 0, 0)

    def left(self, power, second=None):
        drive.set_motor_model(power, power, -power, -power)
        if second is not None:
            time.sleep(second)
            drive.set_motor_model(0, 0, 0, 0)

    def sLeft(self, power, second=None):
        drive.set_motor_model(power, -power, -power, power)
        if second is not None:
            time.sleep(second)
            drive.set_motor_model(0, 0, 0, 0)

    def sRight(self, power, second=None):
        drive.set_motor_model(-power, power, power, -power)
        if second is not None:
            time.sleep(second)
            drive.set_motor_model(0, 0, 0, 0)

    def dRight(self, power, second=None):
        drive.set_motor_model(-power, 0, 0, -power)
        if second is not None:
            time.sleep(second)
            drive.set_motor_model(0, 0, 0, 0)

    def dLeft(self, power, second=None):
        drive.set_motor_model(0, -power, -power, 0)
        if second is not None:
            time.sleep(second)
            drive.set_motor_model(0, 0, 0, 0)
    def stop(self):
        drive.set_motor_model(0,0,0,0)

class IRMovement(Movement):
    def __init__(self):
        self.lastmv = 0

    def IRLights(self):
        right = bool(infrared.read_one_infrared(1))
        center = bool(infrared.read_one_infrared(2))
        left = bool(infrared.read_one_infrared(3))

        if not center:
            self.forward(700)
        if not right:
            self.lastmv = 1
            self.left(650)
        if not left:
            self.right(650)
            self.lastmv = 2
        if center and left and right:
            self.backward(600,0.2)

class ServoUS:
    def __init__(self):
        self.leftSide = False
        self.rightSide = False
        self.objectPresent = False

    def sweepSides(self):
        self.leftSide = False
        self.rightSide = False

        servo.set_servo_pwm("1", 90)  # level
        servo.set_servo_pwm("0", 170)  # left
        time.sleep(0.5)
        dist = dist_sensor.get_distance()
        if dist <= 5:
            self.leftSide = True

        time.sleep(0.2)
        servo.set_servo_pwm("0", 10)  # right
        time.sleep(0.8)
        dist = dist_sensor.get_distance()
        if dist <= 5:
            self.rightSide = True

        print(f"left side = {self.leftSide}")
        print(f"right side = {self.rightSide}")

        servo.set_servo_pwm("1", baseVerticalAngle)
        servo.set_servo_pwm("0", baseHorizontalAngle)
        time.sleep(0.3)

    def ObjectDetect(self):
        servo.set_servo_pwm("1", baseVerticalAngle)
        dist = dist_sensor.get_distance()
        if dist <= 5:
            self.objectPresent = True
            print("Object detected:", self.objectPresent)
            self.sweepSides()
        else:
            self.objectPresent = False
            print("Object detected:", self.objectPresent)
        time.sleep(0.2)

class ColorDetector:
    def __init__(self):
        pass

    def detectColor(self, imageName, rangeLow, rangeHigh, wantedColor):
        img = cv2.imread(imageName)
        if img is None:
            print("Error: Image file not found or could not be read.")
            return

        print("Image Read")
        hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        print("Color Scheme successfully changed to HSV")

        color_mask = cv2.inRange(hsvFrame, rangeLow, rangeHigh)
        print("Color Mask successfully applied")

        white_pixel_count = cv2.countNonZero(color_mask)
        pixel_threshold = 7000
        if white_pixel_count >= pixel_threshold:
            print(f"{wantedColor} Found!!!")
            print(f"There are at least {pixel_threshold} correct pixels here")
        else:
            print(f"{wantedColor} not Found!!!")

    def Detector(self):
        picam2.capture_file("tempImage.jpg")

        if os.path.exists("tempImage.jpg"):
            print("tempImage created")
        else:
            print("tempImage not created")
            return

        # Blue
        self.detectColor("tempImage.jpg",
                         np.array([100, 200, 85], np.uint8),
                         np.array([122, 255, 255], np.uint8),
                         "Blue")

        # Red
        self.detectColor("tempImage.jpg",
                         np.array([0, 155, 149], np.uint8),
                         np.array([9, 255, 255], np.uint8),
                         "Red")

        # Green
        self.detectColor("tempImage.jpg",
                         np.array([38, 98, 141], np.uint8),
                         np.array([60, 255, 255], np.uint8),
                         "Green")

        try:
            if os.path.exists("tempImage.jpg"):
                os.remove("tempImage.jpg")
                print("File tempImage.jpg deleted successfully.")
            else:
                print("File tempImage.jpg does not exist.")
        except OSError as e:
            print("Error deleting file:", e)

class LightResistor(Movement):
    def __init__(self):
        super().__init__()
        self.adc = adc  # Store reference to globally created adc
        self.threshold = None

    def checkThreshold(self):
        for _ in range(10):
            left_idr = self.adc.read_adc(0)
            right_idr = self.adc.read_adc(1)
            print(f"Left IDR: {left_idr}V, Right IDR: {right_idr}V")

        self.threshold = float(input("What would you like as your threshold? "))
        print(f"Threshold set to {self.threshold}")

    def depthLight(self):
        if self.threshold is None:
            print("Threshold not set. Please run checkThreshold() first.")
            return False

        left_idr = self.adc.read_adc(0)
        right_idr = self.adc.read_adc(1)
        print(f"Left IDR: {left_idr}V, Right IDR: {right_idr}V")
        time.sleep(0.1)

        if left_idr >= self.threshold or right_idr >= self.threshold:
            self.left(800, 3)
            return True 

        return False