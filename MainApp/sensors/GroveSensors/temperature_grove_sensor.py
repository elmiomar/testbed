from .grove_sensor import *

"""
This class is the class that retrieves the data from the Temperature Grove sensor.
It inherits from the Grove Sensor class
"""


class TemperatureGroveSensor(GroveSensor):

    def __init__(self, parameters):
        pin_number = parameters['pin_number']
        GroveSensor.__init__(self, pin_number)
        grovepi.pinMode(self.pin_number, "INPUT")
        [temperature_sensor_value, trash] = grovepi.dht(self.pin_number, 0)
        self.timestamp = str(round(time.time(), 3))
        self.value = temperature_sensor_value
