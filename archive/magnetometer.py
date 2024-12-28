""" Display magnetometer data once per second """
import time
import board
import adafruit_lis2mdl
import busio

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lis2mdl.LIS2MDL(i2c)

while True:
	mag_x, mag_y, mag_z = sensor.magnetic
	print("X:{0:10.2f}, Y:{1:10.2f}, Z:{2:10.2f} uT".format(mag_x, mag_y, mag_z))
	print("")
	time.sleep(0.5)