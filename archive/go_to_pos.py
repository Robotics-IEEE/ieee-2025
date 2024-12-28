import os

import sys, tty, termios
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
def getch():
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

from dynamixel_sdk import *                    # Uses Dynamixel SDK library
# Control table addresses and other constants (THIS IS SPECIFIC FOR EACH TYPE OF DYNAMIXEL)
ADDR_MX_TORQUE_ENABLE = 24 
ADDR_MX_GOAL_POSITION = 30
ADDR_MX_PRESENT_POSITION = 36
PROTOCOL_VERSION = 1.0
DEVICENAME = "/dev/ttyUSB0" # TODO: adjust if needed
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
MAX_POS_VAL = 1023 
MIN_POS_VAL = 0 
instanceList = []

class Dynamixel:
    def __init__(self, id: int = None, baud: int = None):
        self.id = id
        self.baud = baud
        self.portHandle = None
        self.packetHandler = None
        instanceList.append(self)

        # Enables torque
        # packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)

    def set_pos(self, pos:int = None):
        self.packetHandler.write2ByteTxRx(self.portHandler, self.id, ADDR_MX_GOAL_POSITION, pos)

    def get_pos(self) -> str:
        dxl_present_position = self.packetHandler.read2ByteTxRx(self.portHandler, self.id, ADDR_MX_PRESENT_POSITION)
        r_string:str = f"PresPos:{dxl_present_position}"
        return r_string

    @staticmethod
    def open_port(self):
        self.portHandler = PortHandler(DEVICENAME)
        self.packetHandler = PacketHandler(PROTOCOL_VERSION) 
        self.portHandler.openPort()
        self.portHandler.setBaudRate(self.baud)

    @staticmethod
    def close_port(self):
        self.packetHandler.write1ByteTxRx(self.portHandler, self.id, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
        self.portHandler.closePort()


