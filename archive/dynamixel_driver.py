import archive.dynamixel_handler as dynamixel_handler
import time

dynamixel_handler.Dynamixel(6, 1000000)
dynamixel_handler.Dynamixel(5, 1000000)
idList = dynamixel_handler.instanceList
idList[1].open_port(idList[1])
idList[0].open_port(idList[0])
idList[0].set_pos(200)
time.sleep(1)
print(idList[0].get_pos())
idList[1].set_pos(800)
time.sleep(1)
print(idList[1].get_pos())

time.sleep(1)

idList[0].set_pos(800)
time.sleep(1)
print(idList[0].get_pos())
idList[1].set_pos(200)
time.sleep(1)
print(idList[1].get_pos())