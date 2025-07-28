import time
from motor import Ordinary_Car
from adc import ADC
adc = ADC()
drive = Ordinary_Car()
import movement

try:
	i = 0
	while i < 10:
		left_idr = adc.read_adc(0)
		right_idr = adc.read_adc(1)
		print(f"Left Idr: {left_idr}V, Right Idr: {right_idr}V")
		i = i+1
	threshold = input("what would you like as your threshold?")
	while True:
		left_idr = adc.read_adc(0)
		right_idr = adc.read_adc(1)
		print(f"Left Idr: {left_idr}V, Right IDR: {right_idr}V")
		time.sleep(1)
		if left_idr >=float(threshold) or right_idr >= float(threshold):
			movement.left(800,3)
except KeyboardInterrupt:
	adc.close_i2c()
