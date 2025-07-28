from infrared import Infrared
from motor import Ordinary_Car
import time

drive = Ordinary_Car()
infrared = Infrared()

while True:
    right = infrared.read_one_infrared(1)
    center = infrared.read_one_infrared(2)
    left = infrared.read_one_infrared(3)
    print(f"({left}, {center}, {right})")

    if not center and right and left:
        drive.set_motor_model(1000,1000,1000,1000)
    elif not right and left:
        drive.set_motor_model(-900,-900,900,900)
    elif not left and right:
        drive.set_motor_model(900,900,-900,-900)
    elif center and left and right:
        drive.set_motor_model(0,0,0,0)


