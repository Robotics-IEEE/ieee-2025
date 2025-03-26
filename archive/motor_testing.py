# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import Jetson.GPIO as jGPIO
import minimalmodbus
import serial
import time

instrument = minimalmodbus.Instrument('/dev/ttyTHS1', 1)
instrument.serial.baudrate = 9600
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1

fault_code = instrument.read_register(0x0076, functioncode=3)

if fault_code != 0:
    print(fault_code)
    print("Clearing fault...")
    instrument.write_register(0x0076, 0, functioncode=6)
    time.sleep(1)

instrument.write_register(0x0116, 1, functioncode=6)

instrument.write_register(0x0136, 1, functioncode=6) #  this is very important. we must do this
time.sleep(1)

print("Setting speed...")
speed = 3000
instrument.write_register(0x0056, speed, functioncode=6)  # Set speed
time.sleep(5)
instrument.write_register(0x00D6, 11528, functioncode=6)
time.sleep(1)

print("Continuous Protection Current Off")
instrument.write_register(0x0126, 10, functioncode=6)
time.sleep(2)

#instrument.write_register(0x0086, 10, functioncode=6)
#time.sleep(1)
print(instrument.write_register(0x0066, 0x1, functioncode=6))
time.sleep(1)

while True:
    print("speed", instrument.read_register(0x005F, functioncode=3))
    print("current",instrument.read_register(0x00B6, functioncode=3))
    print("torque", instrument.read_register(0x00D6, functioncode=3))
    time.sleep(1)
'''
while True:
    time.sleep(1)
    speed = speed - 100
    if speed < 0:
        break
    instrument.write_register(0x0056, speed, functioncode=6)  # Set speed
    print("speed fr: ", instrument.read_register(0x005F, functioncode=3))
'''

