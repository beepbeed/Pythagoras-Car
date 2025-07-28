from mpu6050 import mpu6050
import time

sensor = mpu6050(0x68)

def read_sensor_data():
    accel = sensor.get_accel_data()
    gyro = sensor.get_gyro_data()
    temp = sensor.get_temp()
    return accel, gyro, temp

try:
    while True:
        accel, gyro, temp = read_sensor_data()
        print("Accelerometer:", accel)
        print("Gyroscope:", gyro)
        print("Temperature:", temp, "°C")
        print("-" * 40)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopped by user.")
except Exception as e:
    print("Error:", e)