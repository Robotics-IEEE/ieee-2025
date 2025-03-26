import minimalmodbus
import serial
import time

# TODO: fix these
DRIVETRAIN_TORQUE_CODE = 9928
INTAKE_TORQUE_CODE = 11528

class Motor:
    def __init__(self, id:int = None, drivetrain:bool = True):
        self.id = id
        self.speed = 0
        self.drivetran = drivetrain
    
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
            print(f"Old fault {fault_code} detected. Clearing fault...")
            self.instrument.write_register(0x0076, 0, functioncode=6)
            time.sleep(0.1)

        print("Resetting speed...")
        self.instrument.write_register(0x0056, self.speed, functioncode=6)  # Set speed
        time.sleep(1)

        print("Resetting torque...")
        if self.drivetrain:
            self.instrument.write_register(0x00D6, DRIVETRAIN_TORQUE_CODE, functioncode=6)
        else:
            self.instrument.write_register(0x00D6, INTAKE_TORQUE_CODE, functioncode=6)

        print("Starting motor...")
        self.instrument.write_register(0x0066, 0, functioncode=6)  # Start forward rotation
        time.sleep(1)
        
        self.instrument.write_register(0x0136, 1, functioncode=6) #this is very important. we must do this
        time.sleep(1)

        print(f"Motor {id} ready.")


    def move_forward(self, speed, time=None): 
        self.speed = speed
        self.instrument.write_register(0x0066, 1, functioncode=6)  # Start forward rotation
        
        if self.drivetrain:
            self.instrument.write_register(0x00D6, DRIVETRAIN_TORQUE_CODE, functioncode=6)
        else:
            self.instrument.write_register(0x00D6, INTAKE_TORQUE_CODE, functioncode=6)
        if time is not None:
            time.sleep(time)

        self.instrument.write_register(0x0056, speed, functioncode=6)

    def move_reverse(self, speed, time=None): 
        self.speed = speed
        self.instrument.write_register(0x0066, 2, functioncode=6)  # Start reverse rotation
        
        if self.drivetrain:
            self.instrument.write_register(0x00D6, DRIVETRAIN_TORQUE_CODE, functioncode=6)
        else:
            self.instrument.write_register(0x00D6, INTAKE_TORQUE_CODE, functioncode=6)
        if time is not None:
            time.sleep(time)
    
        self.instrument.write_register(0x0056, speed, functioncode=6)
