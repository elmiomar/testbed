from .grove_sensor import *

"""
This class is the class that retrieves the data from the Ultrasonic Grove sensor.
It inherits from the Grove Sensor class
"""


class UltrasonicGroveSensor(GroveSensor):

    def __init__(self, parameters):
        pin_number = parameters['pin_number']
        GroveSensor.__init__(self, pin_number)
        grovepi.pinMode(self.pin_number, "INPUT")
        ultrasonic_sensor_value = grovepi.ultrasonicRead(self.pin_number)
        self.timestamp = str(round(time.time(), 3))
        self.value = ultrasonic_sensor_value
