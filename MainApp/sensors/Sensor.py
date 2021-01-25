"""
This class is the parent class that describes a sensor
"""


class Sensor:

    """
    Function to initialize the variables.
    """
    def __init__(self):
        self._unit = None
        self._timestamp = None
        self._value = None
        self._uncertainty = None
        self._manufacturer_specifications = None
        self._type = None
        self._location = None
        self._topic = None

    """
    Function to get/set to access the attributes of Sensor.
    """
    def get_uncertainty(self):
        return self.uncertainty

    def set_uncertainty(self, uncertainty):
        self.uncertainty = uncertainty

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_unit(self):
        return self.unit

    def set_unit(self, unit):
        self.unit = unit

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_manufacturer_specifications(self):
        return self.manufacturer_specifications

    def set_manufacturer_specifications(self,manufacturer_specifications):
        self.manufacturer_specifications = manufacturer_specifications

    def get_topic(self):
        return self._topic

    def set_topic(self, topic):
        self.topic = topic

    _uncertainty = property(get_uncertainty, set_uncertainty)
    _type = property(get_type, set_type)
    _manufacturer_specifications = property(get_manufacturer_specifications, set_manufacturer_specifications)
    _location = property(get_location, set_location)
    _unit = property(get_unit, set_unit)
    _timestamp = property(get_timestamp, set_timestamp)
    _value = property(get_value, set_value)
    _topic = property(get_topic, set_topic)
