
from led_light import Led_Light
from pedestrian_button import Pedestrian_Button
from controller import TrafficLightSubsystem, PedestrianSubsystem
# from audio_notification import Audio_Notification
from time import time, sleep

led_pedestrian_red = Led_Light(19, True, True)
led_pedestrian_green = Led_Light(17, False, True)
led_traffic_red = Led_Light(3, False, True)
led_traffic_amber = Led_Light(5, False, True)
led_traffic_green = Led_Light(6, False, True)
Pedestrian_Button = Pedestrian_Button(22, True, True)
buzzer = Audio_Notification(27, True)

light = TrafficLightSubsystem(red, amber, green, True)

'''
def Traffic_Subsytem_Driver():
    def Idle():
        TrafficLightSubsystem.show_red()
'''

def Traffic_Subsystem_Driver():
    print("Testing Traffic Light in 5 seconds")
    sleep(5)
    light.show_red()
    print("Pass if: Red ON, Amber Off, Green Off")
    sleep(10)
    light.show_amber()
    print("Pass if: Red Off, Amber On, Green Off")
    sleep(10)
    light.show_green()
    print("Pass if: Red Off, Amber Off, Green On")
    sleep(10)

Traffic_Subsystem_Driver()