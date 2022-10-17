from machine import Pin, PWM
import utime

led = Pin(25, Pin.OUT)
led.value(1)

pwm_red = PWM(Pin(16))
pwm_green = PWM(Pin(18))
pwm_blue = PWM(Pin(20))

pwm_red.freq(100)
pwm_green.freq(100)
pwm_blue.freq(100)

while True:

    for x in range (1,101):
        pwm_green.duty_u16(int(x * 0.01 * 32768))
        utime.sleep(0.025)
    for x in range (1,101):
        pwm_red.duty_u16(int(32768 - x * 0.01 * 32768))
        utime.sleep(0.025)
    for x in range(1,101):
        pwm_green.duty_u16(int(32768 - x * 0.01 * 32768))
        pwm_blue.duty_u16(int(x * 0.01 * 32768))
        utime.sleep(0.025)
    for x in range(1,101):
        pwm_red.duty_u16(int(x * 0.01 * 32768))
        utime.sleep(0.025)
        

    