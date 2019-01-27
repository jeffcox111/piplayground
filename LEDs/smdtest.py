import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

green = 18
red = 23
blue = 24


GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

GPIO.output(green, 255)
GPIO.output(red, 200)
GPIO.output(blue, 200)
