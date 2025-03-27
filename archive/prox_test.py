import Jetson.GPIO as GPIO
import time

GPIO.setwarnings(False)

# set correct channel
prox_channel = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(prox_channel, GPIO.IN)

def update_proximity(channel):
    prox_detected = GPIO.input(channel)

    print(f"Proximity: {prox_detected}")

GPIO.add_event_detect(prox_channel, GPIO.BOTH, callback=update_proximity)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    GPIO.cleanup()
