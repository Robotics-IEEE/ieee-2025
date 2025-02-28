import Jetson.GPIO as GPIO
import time

# Disable warnings
GPIO.setwarnings(False)

# Define GPIO pins for A+ / A- and B+ / B-
A_plus = 17
A_minus = 18
B_plus = 27
B_minus = 22

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up GPIO pins as inputs without pull-up/down resistors
GPIO.setup(A_plus, GPIO.IN)
GPIO.setup(A_minus, GPIO.IN)
GPIO.setup(B_plus, GPIO.IN)
GPIO.setup(B_minus, GPIO.IN)

position = 0
last_A_plus = GPIO.input(A_plus)
last_B_plus = GPIO.input(B_plus)

def update_encoder(channel):
    global position, last_A_plus, last_B_plus

    # Read the current states of A+ / A-, and B+ / B-
    A_plus_state = GPIO.input(A_plus)
    A_minus_state = GPIO.input(A_minus)
    B_plus_state = GPIO.input(B_plus)
    B_minus_state = GPIO.input(B_minus)

    # Correct differential signaling processing (checking if A+ is inverted from A-)
    if A_plus_state != A_minus_state and B_plus_state != B_minus_state:
        # Determine direction based on phase shift between A+ and B+
        if last_A_plus == 0 and A_plus_state == 1:  # Rising edge of A+
            if B_plus_state == 0:
                position += 1  # Clockwise (CW)
            else:
                position -= 1  # Counter-Clockwise (CCW)
        elif last_B_plus == 0 and B_plus_state == 1:  # Rising edge of B+
            if A_plus_state == 1:
                position += 1  # Clockwise (CW)
            else:
                position -= 1  # Counter-Clockwise (CCW)

    last_A_plus = A_plus_state
    last_B_plus = B_plus_state

    print(f"Position: {position}")

# Set up interrupts for A+ and B+ signals
GPIO.add_event_detect(A_plus, GPIO.BOTH, callback=update_encoder)
GPIO.add_event_detect(B_plus, GPIO.BOTH, callback=update_encoder)

try:
    while True:
        time.sleep(1)  # Keeping the script alive for event detection

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    GPIO.cleanup()


"""
import serial
import Jetson.GPIO as GPIO
import time

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
A_plus = 17
A_minus = 18
B_plus = 27
B_minus = 22

# Set up GPIO pins as inputs
GPIO.setup(A_plus, GPIO.IN)
GPIO.setup(A_minus, GPIO.IN)
GPIO.setup(B_plus, GPIO.IN)
GPIO.setup(B_minus, GPIO.IN)

try:
    while True:
        # Read the encoder signals
        A_plus_state = GPIO.input(A_plus)
        A_minus_state = GPIO.input(A_minus)
        B_plus_state = GPIO.input(B_plus)
        B_minus_state = GPIO.input(B_minus)
        
        # Process the encoder signals
        # (Implement your logic here)
        #        print("A+: {A_plus_state}, A-: {A_minus_state}, B+: {B_plus_state}, B-: {B_minus_state}")
        print("[A+: ", A_plus_state, ", A-: ", A_minus_state, "B+: ", B_plus_state, "B-: ", B_minus_state,"]")
        
        time.sleep(0.01)  # Adjust the sleep time as needed

except KeyboardInterrupt:
    print("Program terminated.")

finally:
    GPIO.cleanup()
"""


