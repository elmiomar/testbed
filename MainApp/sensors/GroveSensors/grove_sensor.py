from ..Sensor import *
import grovepi
import time

"""
Class used to describe the message to send to retrieve the value of a grove sensor.
It inherits from the Sensor class
"""


class GroveSensor(Sensor):
    """
    Function to initialize the variables.
    """
    def __init__(self,pin_number):
        Sensor.__init__(self)
        self.pin_number = pin_number

    """
    Function to get/set to access the attributes of Grove Sensor.
    """
    def get_pin_number(self):
        return self.pin_number

    def set_pin_number(self,pin_number):
        self.pin_number = pin_number

    pinNumber=property(get_pin_number, set_pin_number)
