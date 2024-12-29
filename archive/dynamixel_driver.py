from dynamixel_handler import DynamixelHandler
import time

handler = DynamixelHandler(1000000)
DYN_1 = 8
DYN_2 = 5

handler.add_dynamixel(DYN_1)
handler.add_dynamixel(DYN_2)

handler.open_port()

handler.set_pos(DYN_1, 200)
time.sleep(1)
handler.set_pos(DYN_1, 800)
time.sleep(1)

handler.set_pos(DYN_2, 200)
time.sleep(1)
handler.set_pos(DYN_2, 800)
time.sleep(1)

handler.close_port()
