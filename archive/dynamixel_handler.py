from dynamixel_sdk import PortHandler, PacketHandler

ADDR_MX_TORQUE_ENABLE = 24
ADDR_MX_GOAL_POSITION = 30
ADDR_MX_PRESENT_POSITION = 36
PROTOCOL_VERSION = 1.0
DEVICENAME = "/dev/ttyUSB0"
TORQUE_ENABLE = 1
TORQUE_DISABLE = 0
MAX_POS_VAL = 1023
MIN_POS_VAL = 0 

class DynamixelHandler:
    def __init__(self, baud: int = 1000000):
        self.port_handler = None
        self.packet_handler = None
        self.connected = []
        self.is_port_active = False
        self.baud = baud

    def add_dynamixel(self, dynamixel_id: int):
        self.connected.append(dynamixel_id)

    def remove_dynamixel(self, dynamixel_id: int):
        self.connected.remove(dynamixel_id)

    def set_pos(self, dynamixel_id: int, pos: int):
        try:
            self.packet_handler.write2ByteTxRx(self.port_handler, dynamixel_id, ADDR_MX_GOAL_POSITION, pos)
        except Exception as e:
            return e

    def get_pos(self, dynamixel_id: int):
        dxl_present_position = self.packet_handler.read2ByteTxRx(self.port_handler, dynamixel_id, ADDR_MX_PRESENT_POSITION)
        return dxl_present_position
    
    def set_torque(self, dynamixel_id: int):
        try:
            self.packet_handler.write1ByteTxRx(self.port_handler, dynamixel_id, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
        except Exception as e:
            return e

    def open_port(self):
        self.port_handler = PortHandler(DEVICENAME)
        self.packet_handler = PacketHandler(PROTOCOL_VERSION) 
        self.port_handler.openPort()
        self.port_handler.setBaudRate(self.baud)
        print("Dynamixel port opened.")
        self.is_port_active = True

    def close_port(self):
        for id in self.connected:
            self.packet_handler.write1ByteTxRx(self.port_handler, id, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
        self.port_handler.closePort()
        print("Dynamixel port closed.")
        self.is_port_active = False

    def is_port_active(self):
        return self.is_port_active
