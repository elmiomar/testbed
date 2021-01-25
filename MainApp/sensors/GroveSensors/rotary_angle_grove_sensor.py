from .grove_sensor import *

"""
This class is the class that retrieves the data from the Rotary Angle Grove sensor.
It inherits from the Grove Sensor class
"""


class RotaryAngleGroveSensor(GroveSensor):

    def __init__(self, parameters):
        pin_number = parameters['pin_number']
        GroveSensor.__init__(self, pin_number)
        grovepi.pinMode(self.pin_number, "INPUT")
        sensor_value = grovepi.analogRead(self.pin_number)
        self.timestamp = str(round(time.time(), 3))
        adc_ref = 5  # Reference voltage of ADC is 5v
        grove_vcc = 5  # Vcc of the grove interface is normally 5
        full_angle = 300  # Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
        voltage = round(float(sensor_value) * adc_ref / 1023, 2)
        degrees = round((voltage * full_angle) / grove_vcc, 2)
        self.value = degrees
