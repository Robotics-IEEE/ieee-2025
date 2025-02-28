# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import Jetson.GPIO as jGPIO
import minimalmodbus
import serial
import time

EN_PIN = 13
 
jGPIO.setmode(jGPIO.BCM)
jGPIO.setup(EN_PIN, GPIO.OUT)
jGPIO.output(EN_PIN, GPIO.LOW)
 
pwm = jGPIO.PWM(EN_PIN, 100)
pwm.start(0)
 
instrument = minimalmodbus.Instrument('/dev/ttyTHS1', 1)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1

time.sleep(2)
 
try:
    print("Reading initial fault code...")
    fault_code = instrument.read_register(0x0076, functioncode=3)
    print(f"Fault code: {fault_code}")
 
    if fault_code != 0:
        print("Clearing fault...")
        instrument.write_register(0x0076, 0, functioncode=6)
        time.sleep(0.1)
 
    print("Setting speed...")
#    instrument.write_register(0x0056, 1000, functioncode=6)  # Set speed
    time.sleep(1)
 

    print("Starting motor...")

#    instrument.write_register(0x0066, 1, functioncode=6)  # Start forward rotation
    time.sleep(1)
    
#    instrument.write_register(0x0136, 1, functioncode=6) // this is very important. we must do this
    time.sleep(1)
 
    while True:
        print("read: err", instrument.read_register(118, functioncode=3))
        print("on: ", instrument.read_register(102, functioncode=3))
        print("speed: ", instrument.read_register(86, functioncode=3))
        time.sleep(2)
 
finally:
    jGPIO.cleanup()
 


"""

	print(instrument.read_register(0x0066, functioncode=3))
	time.sleep(5)
	instrument.write_register(0x0066, 0x1, functioncode=6)
	time.sleep(5)
	print(instrument.read_register(0x0066, functioncode=3))
	time.sleep(5)
	instrument.write_register(0x0066, 0x1, functioncode=6)

	print(instrument.read_register(0x0076, functioncode=3))
	time.sleep(3)
	
	instrument.write_register(0x0066, 1, functioncode=6)
	print(instrument.read_register(0x0066, functioncode=3))
	print("slave id", instrument.read_register(0x00A6, functioncode=3))
	time.sleep(2)

	instrument.write_register(0x00D6, 3, functioncode=6)
	pwm.ChangeDutyCycle(100)
	time.sleep(2)

	speed_val = 50
	instrument.write_register(0x0056, speed_val, functioncode=6)
	print(instrument.read_register(0x0056, functioncode=3))

	time.sleep(10)

	print(instrument.read_register(0x005F, functioncode=3))

	time.sleep(2)
"""

