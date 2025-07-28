from hardware import Movement, IRMovement, ServoUS, ColorDetector, LightResistor
import time

motor = Movement()
robot = IRMovement()
obstacle = ServoUS()
vision = ColorDetector()
ldr = LightResistor()

try:
    ldr.checkThreshold()
    while True:
        robot.IRLights()
        obstacle.ObjectDetect()
        if ldr.depthLight():
            print("Breaking from loop due to light condition.")
            break
        time.sleep(0.05)
except KeyboardInterrupt:
    print("Shutting down robot.")
finally:
    motor.stop()
    ldr.adc.close_i2c()
