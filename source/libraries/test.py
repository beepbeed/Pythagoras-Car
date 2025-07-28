from motor import Ordinary_Car
drive = Ordinary_Car()
import time
# relative to the front
# bottom right
drive.set_motor_model(1000,0,0,0)
time.sleep(1)
# top right
drive.set_motor_model(0,1000,0,0)
time.sleep(1)
# bottom left
drive.set_motor_model(0,0,1000,0)
time.sleep(1)
# top left
drive.set_motor_model(0,0,0,1000)
time.sleep(1)
drive.set_motor_model(0,0,0,0)
