from machine import Pin
from time import time, sleep
from v03 import Led_Light


led = Led_Light(3, flashing=True, debug=True)

print("Testing on()")
led.on()
if led.value() == 1:
    print(".on() passed")
sleep(1)
led.off()
if led.value() == 0:
    print(".off passed")
led.toggle()
if led.value() == 1:
    print("toggle on passed")
sleep(1)
if led.value() == 0:
    print("toggle off passed")
sleep(1)
state = led.led_light_state
if state == 0:
    print("state off")
elif state == 1:
    print("state on")