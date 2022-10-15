from machine import Pin
import utime

red = Pin(16, Pin.OUT)
green = Pin(18, Pin.OUT)
blue = Pin(20, Pin.OUT)

led = Pin(25, Pin.OUT)
led.value(1)

while True:

    for x in range (1,101):
        green.value(x)
        utime.sleep(0.025)
    for x in range (1,101):
        red.value(101-x)
        utime.sleep(0.025)
    for x in range(1,101):
        green.value(101-x)
        blue.value(x)
        utime.sleep(0.025)
    for x in range(1,101):
        red.value(x)
        utime.sleep(0.025)
        

    