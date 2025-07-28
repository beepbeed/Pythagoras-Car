from motor import Ordinary_Car
import time 

drive = Ordinary_Car()

def forward(power, second):
	drive.set_motor_model(-power,-power,-power,-power)
	time.sleep(second)
	drive.set_motor_model(0,0,0,0)
def backward(power, second):
	drive.set_motor_model(power,power,power,power)
	time.sleep(second)
	drive.set_motor_model(0,0,0,0)
def right(power, second):
	drive.set_motor_model(-power,-power,power,power)
	time.sleep(second)
	drive.set_motor_model(0,0,0,0)
def left(power, second):
	drive.set_motor_model(power,power,-power,-power)
	time.sleep(time)
	drive.set_motor_model(0,0,0,0)
def sLeft(power, second):
	drive.set_motor_model(power,-power,-power,power)
	time.sleep(second)
	drive.set_motor_model(0,0,0,0)
def sRight(power, second):
	drive.set_motor_model(-power,power,power,-power)
	time.sleep(second)
	drive.set_motor_model(0,0,0,0)
def dRight(power,second):
	drive.set_motor_model(-power,0,0,-power)
	time.sleep(second)
	drive.set_motor_model(0,0,0,0)
def dLeft(power,second):
	drive.set_motor_model(0,-power,-power,0)
	time.sleep(second)
	drive.set_motor_model(0,0,0,0)