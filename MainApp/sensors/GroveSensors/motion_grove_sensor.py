from .grove_sensor import *

"""
This class is the class that retrieves the data from the Motion Grove sensor.
It inherits from the Grove Sensor class
"""


class MotionGroveSensor(GroveSensor):

    def __init__(self, parameters):
        pin_number = parameters['pin_number']
        GroveSensor.__init__(self, pin_number)
        grovepi.pinMode(self.pin_number, "INPUT")
        motion_sensor_value = grovepi.digitalRead(self.pin_number)  # Sense motion, usually human, within the target range
        self.timestamp = str(round(time.time(), 3))
        if motion_sensor_value == 0 or motion_sensor_value == 1:  # check if reads were 0 or 1 it can be 255 also because of IO Errors so remove those values
            self.value = motion_sensor_value
            time.sleep(.2)  # if your hold time is less than this, you might not see as many detections



