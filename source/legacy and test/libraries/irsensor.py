from infrared import Infrared
from motor import Ordinary_Car
import time
import movement 

drive = Ordinary_Car()
infrared = Infrared()
lastmv = 0

while True:
    right = bool((infrared.read_one_infrared(1)))
    center = bool((infrared.read_one_infrared(2)))
    left = bool((infrared.read_one_infrared(3)))

    print(f"({left}, {center}, {right})")

    if not center: #calibrate to width of tape
        movement.forward(700)
    if not right:
	lastmv = 1
        movement.left(650)
    if not left:
        movement.right(650)
	lastmv = 2
    if center and left and right:
        if lastmv == 1:
		movement.right(600)
	if lastmv == 2:
		movement.left(600)
	else:
		movement.backward(600)
    
    time.sleep(0.075)
    #try:
    
    """
        #time.sleep(0.1)
    except Exception:
        drive.set_motor_model(0,0,0,0)
        print("Weird issue with OSError (errno5 or errno110)")
        print("Also, STOPED")
        break
    """

