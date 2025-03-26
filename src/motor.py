import minimalmodbus
import serial
import time


class Motor:
    def __init__(self, id:int = None):
        self.id = id
        self.speed = 0
    
    @classmethod
    def setup(self):   
        self.instrument = minimalmodbus.Instrument('/dev/ttyTHS1', self.id)
        self.instrument.serial.baudrate = 9600
        self.instrument.serial.bytesize = 8
        self.instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
        self.instrument.serial.stopbits = 1
        self.instrument.serial.timeout = 1
        print("Reading initial fault code...")
        fault_code = self.instrument.read_register(0x0076, functioncode=3)
        print(f"Fault code: {fault_code}")

        if fault_code != 0:
            print("Clearing fault...")
            self.instrument.write_register(0x0076, 0, functioncode=6)
            time.sleep(0.1)

        print("Setting speed...")
        self.instrument.write_register(0x0056, self.speed, functioncode=6)  # Set speed
        time.sleep(1)

        print("Starting motor...")

        self.instrument.write_register(0x0066, 1, functioncode=6)  # Start forward rotation
        time.sleep(1)
        
        self.instrument.write_register(0x0136, 1, functioncode=6) #this is very important. we must do this
        time.sleep(1)


    def set_speed(self, speed): 
        self.speed = speed 
        self.instrument.write_register(0x0056, speed, functioncode=6)

    def set_speed_time(self, speed, time):
        self.speed = speed
        self.instrument.write_register(0x0056, speed, functioncode=6)
        time.sleep(time)
