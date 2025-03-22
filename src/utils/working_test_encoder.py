import Jetson.GPIO as GPIO
import time

GPIO.setwarnings(False)

# Define GPIO pins for A+ / A- and B+ / B-
A_plus = 17
A_minus = 18
B_plus = 27
B_minus = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(A_plus, GPIO.IN)
GPIO.setup(A_minus, GPIO.IN)
GPIO.setup(B_plus, GPIO.IN)
GPIO.setup(B_minus, GPIO.IN)

position = 0
last_A_plus = GPIO.input(A_plus)
last_B_plus = GPIO.input(B_plus)

def update_encoder(channel):
    global position, last_A_plus, last_B_plus

    A_plus_state = GPIO.input(A_plus)
    A_minus_state = GPIO.input(A_minus)
    B_plus_state = GPIO.input(B_plus)
    B_minus_state = GPIO.input(B_minus)

    if A_plus_state != A_minus_state and B_plus_state != B_minus_state:
        if last_A_plus == 0 and A_plus_state == 1:
            if B_plus_state == 0:
                position += 1
            else:
                position -= 1
        elif last_B_plus == 0 and B_plus_state == 1:
            if A_plus_state == 1:
                position += 1
            else:
                position -= 1

    last_A_plus = A_plus_state
    last_B_plus = B_plus_state

    print(f"Position: {position}")

GPIO.add_event_detect(A_plus, GPIO.BOTH, callback=update_encoder)
GPIO.add_event_detect(B_plus, GPIO.BOTH, callback=update_encoder)

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    GPIO.cleanup()