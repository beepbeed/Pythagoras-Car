import RPi.GPIO as GPIO
import time
from hx711 import HX711 #https://pypi.org/project/hx711/

def read(x):
    try:
        y=x.get_raw_data_mean()
    except Exception:
        return False
    else:
        return y
def connect(name, int(dout), int(sckp)):
    try:
        GPIO.setmode(GPIO.BCM) #https://github.com/gandalf15/HX711/blob/master/python_examples/simple_example.py    
        name = HX711(
            dout_pin=dout, #pin 5
            pd_sck_pin=sckp, #pin 6
            channel='A', #idk this one
            gain=64 #also dont know this one
        )
        hx711.reset()   # Before we start, reset the HX711 (not obligate)
        """
        measures = hx711.get_raw_data(num_measures=3)
        #print(measures)
        """
        return True
    except Exception:
        return False

## attempt conn ##

hx711 = None
connect(hx711, 5, 6)

## loop ##

while True:
    tempMeasure = read(hx711)
    if tempMeasure == False:
        i = 0
        print("Connection failure.")
        while i < 10:
            print(f"Reconnecting session {1+i}...")
            if connect(hx711, 5, 6):
                print("Reconnected successfully.")
                break
            i+=1
            time.sleep(0.1)
    else:
        print(tempMeasure)
    time.sleep(0.5)
            
            
        