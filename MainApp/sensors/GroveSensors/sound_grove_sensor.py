from .grove_sensor import *

"""
This class is the class that retrieves the data from the Sound Grove sensor.
It inherits from the Grove Sensor class
"""


class SoundGroveSensor(GroveSensor):

    def __init__(self, parameters):
        pin_number = parameters['pin_number']
        GroveSensor.__init__(self, pin_number)
        grovepi.pinMode(self.pin_number, "INPUT")
        sound_sensor_value = grovepi.analogRead(self.pin_number)
        self.timestamp = str(round(time.time(), 3))
        self.value = sound_sensor_value
