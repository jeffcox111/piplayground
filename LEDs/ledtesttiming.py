import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(11, True)
time.sleep(1)
GPIO.output(5, True)
time.sleep(1)
GPIO.output(6, True)
time.sleep(1)
GPIO.output(13, True)
time.sleep(1)
GPIO.output(19, True)
time.sleep(1)
GPIO.output(16, True)


