import time
from adc import ADC
adc = ADC()
try:
	while True:
		left_idr = adc.read_adc(0)
		right_idr = adc.read_adc(1)
		print(f"Left Idr: {left_idr}V, Right IDR: {right_idr}V")
		time.sleep(1)
		
except KeyboardInterrupt:
	adc.close_i2c()
