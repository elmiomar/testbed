from .grove_sensor import *

"""
This class is the class that retrieves the data from the Humidity Grove sensor.
It inherits from the Grove Sensor class
"""


class HumidityGroveSensor(GroveSensor):

    def __init__(self, parameters):
        pin_number = parameters['pin_number']
        GroveSensor.__init__(self, pin_number)
        grovepi.pinMode(self.pin_number, "INPUT") #listen to data sensed on the specified pin_number
        [trash, humidity_sensor_value] = grovepi.dht(self.pin_number, 0) #sense
        self.timestamp = str(round(time.time(), 3))  # measure Timestamp
        self.value = humidity_sensor_value #store the sensed value



