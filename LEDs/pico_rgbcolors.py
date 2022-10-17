from machine import Pin, PWM
import utime

# red = Pin(16, Pin.OUT)
# green = Pin(18, Pin.OUT)
# blue = Pin(20, Pin.OUT)

led = Pin(25, Pin.OUT)
led.value(1)

freq = 100

pwm_red=PWM(Pin(16))
pwm_green = PWM(Pin(18))
pwm_blue = PWM(Pin(20))

while True:

    for x in range (1,101):
        pwm_green.duty_u16(x)
        utime.sleep(0.025)
    for x in range (1,101):
        pwm_red.duty_u16(101-x)
        utime.sleep(0.025)
    for x in range(1,101):
        pwm_green.duty_u16(101-x)
        pwm_blue.duty_u16(x)
        utime.sleep(0.025)
    for x in range(1,101):
        pwm_red.duty_u16(x)
        utime.sleep(0.025)
        

    