from time import time, sleep, ticks_diff, ticks_ms
from machine import Pin

class Pedestrian_Button(Pin):
    def __init__(self, pin, debug)
    super.__init__(pin, Pin.IN, Pin.PULL_DOWN)
    self.__debug = debug
    self.__pin = pin
    self.__last_pressed = 0
    self.__pedestrian_waiting = False
    self.button_state


def button_state(self):
    if self.__debug:
        print(f"Button connected to Pin {self.__pin} is {'Waiting' if self.__pedestrian_waiting else 'not waiting'}")
        return self.__pedestrian_wating


def button_state(self, value):
    if self.debug:
        print(f"Button state on Pin {self.pin} set to {value}")

class Pedestrian_Button(Pin):
    def __init__(self, pin, debug):
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)

def callback(self, pin):
    current_time = time.ticks_ms()
    if time.ticks_diff(current_time, self.__last_pressed) > 200:
        self.__last_pressed = current_time
        self.__pedestrian_waiting = True
        if self.__debug:
            print(f"Button pressed on Pin{self.pin} at {current_time}ms")

