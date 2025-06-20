from machine import Pin
from time import sleep, time

class Led_Light(Pin):
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing
        self.__last_toggle_time = time()
    
    def on(self):
        self.high()
        if self.__debug:
            print(f"LED is connected to {self.__pin} is {self.led_light_state}")
    
    def off(self):
        self.low()
        if self.__debug:
            print(f"LED is connected to {self.__pin} is {self.led_light_state}")
    
    def toggle(self):
        if self.value() == 0:
            self.on()
        else:
            self.off()
    
    def led_light_state(self):
        return self.value()
    
    def led_light_state(self, value):
        if value == 1:
            self.off()
        elif value == 0:
            self.on()

def flash(self): 
    now = time()
    if self.__flashing and now - self.__last_toggle_time >= 0.5:
        self.toggle()
        self.__last_toggle_time = now


'''
red_light = Led_light(3, True)
while True:
    red_light.on()
    sleep(0.5)
    red_light.off()
    sleep(0.5) 
while True:
    red_light.led_light_state(1)
    sleep(0.5)
    red_light.led_light_state(0)
    sleep(0.5)
'''
