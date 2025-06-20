'''
A simple script to unit test hardware
'''

from machine import Pin
from machine import PWM

# Pin Documentation: https://docs.micropython.org/en/latest/library/machine.Pin.html
# PWM Documentation: https://docs.micropython.org/en/latest/library/machine.PWM.html
# Pinout: https://datasheets.raspberrypi.com/pico/Pico-R3-Pinout.png

led_car_red = Pin(3, Pin.OUT)
led_car_orange = Pin(5, Pin.OUT)
led_car_green = Pin(6, Pin.OUT)

led_pedestrian_red = Pin(19, Pin.OUT)
led_pedestrian_green = Pin(17, Pin.OUT)

pedestrian_button = Pin(22, Pin.IN, Pin.PULL_DOWN)

<<<<<<< HEAD:project/py_scripts/lights.py
buzzer = machine.PWM(27)
=======
buzzer = PWM(27)
>>>>>>> dee79fb541a3f03e4731cd161ad244f9987e3ee2:project/py_scripts/v02.py
buzzer.freq(1000)


while True:
<<<<<<< HEAD:project/py_scripts/lights.py
=======
    
>>>>>>> dee79fb541a3f03e4731cd161ad244f9987e3ee2:project/py_scripts/v02.py
    buzzer.duty_u16(32768)

    led_car_red.high()
    led_car_orange.high()
    led_car_green.high()

    led_pedestrian_red.high()
    led_pedestrian_green.high()

<<<<<<< HEAD:project/py_scripts/lights.py
<<<<<<< HEAD:project/py_scripts/lights.py

=======
>>>>>>> 76b3ae39324477d41c965023028003a5e4a734e3:project/py_scripts/v02.py
    print(pedestrian_button.value())
=======
    print(pedestrian_button.value())
>>>>>>> dee79fb541a3f03e4731cd161ad244f9987e3ee2:project/py_scripts/v02.py
