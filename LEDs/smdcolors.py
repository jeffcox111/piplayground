import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RUNNING = True
green = 18
red = 23
blue = 24
Freq = 100

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)

try:
	while RUNNING:
		RED.start(100)
		GREEN.start(1)
		BLUE.start(1)

		for x in range (1,101):
			GREEN.ChangeDutyCycle(x)
			time.sleep(0.05)
		for x in range (1,101):
			RED.ChangeDutyCycle(101-x)
			time.sleep(0.025)
		for x in range(1,101):
			GREEN.ChangeDutyCycle(101-x)
			BLUE.ChangeDutyCycle(x)
			time.sleep(0.025)
		for x in range(1,101):
			RED.ChangeDutyCycle(x)
			time.sleep(0.025)

except KeyboardInterrupt:
	RUNNING=False
	GPIO.cleanup()
