import Jetson.GPIO as GPIO
import time

PWM_PIN = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(PWM_PIN, GPIO.OUT, initial=GPIO.LOW)

pwm = GPIO.PWM(PWM_PIN, 100)
pwm.start(0)

try:
	while True:
		for duty in range(0, 101, 10):
			pwm.ChangeDutyCycle(duty)
			time.sleep(4)
			if duty >= 100:
				exit()

except:
	print("hi")
