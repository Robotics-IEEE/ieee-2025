import Jetson.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

class Encoder:
    def __init__(self, a_plus: int, a_minus: int, b_plus: int, b_minus: int):
        self.a_plus = a_plus
        self.a_minus = a_minus
        self.b_plus = b_plus
        self.b_minus = b_minus
        self.position = 0

        GPIO.setup(self.a_plus, GPIO.IN)
        GPIO.setup(self.a_minus, GPIO.IN)
        GPIO.setup(self.b_plus, GPIO.IN)
        GPIO.setup(self.b_minus, GPIO.IN)

    def cleanup(self):
        GPIO.cleanup([self.a_plus, self.a_minus, self.b_plus, self.b_minus]) 

    def update_encoder(self):
        global position, last_A_plus, last_B_plus

        A_plus_state = GPIO.input(self.a_plus)
        A_minus_state = GPIO.input(self.a_minus)
        B_plus_state = GPIO.input(self.b_plus)
        B_minus_state = GPIO.input(self.b_minus)

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