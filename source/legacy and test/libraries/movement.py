from motor import Ordinary_Car
import time 

drive = Ordinary_Car()

def forward(power, second=None):
    drive.set_motor_model(-power, -power, -power, -power)
    if second is not None:
        time.sleep(second)
        drive.set_motor_model(0, 0, 0, 0)

def backward(power, second=None):
    drive.set_motor_model(power, power, power, power)
    if second is not None:
        time.sleep(second)
        drive.set_motor_model(0, 0, 0, 0)

def right(power, second=None):
    drive.set_motor_model(-power, -power, power, power)
    if second is not None:
        time.sleep(second)
        drive.set_motor_model(0, 0, 0, 0)

def left(power, second=None):
    drive.set_motor_model(power, power, -power, -power)
    if second is not None:
        time.sleep(second)
        drive.set_motor_model(0, 0, 0, 0)

def sLeft(power, second=None):
    drive.set_motor_model(power, -power, -power, power)
    if second is not None:
        time.sleep(second)
        drive.set_motor_model(0, 0, 0, 0)

def sRight(power, second=None):
    drive.set_motor_model(-power, power, power, -power)
    if second is not None:
        time.sleep(second)
        drive.set_motor_model(0, 0, 0, 0)

def dRight(power, second=None):
    drive.set_motor_model(-power, 0, 0, -power)
    if second is not None:
        time.sleep(second)
        drive.set_motor_model(0, 0, 0, 0)

def dLeft(power, second=None):
    drive.set_motor_model(0, -power, -power, 0)
    if second is not None:
        time.sleep(second)
        drive.set_motor_model(0, 0, 0, 0)
