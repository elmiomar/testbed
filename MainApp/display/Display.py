import json
import time

"""
This class is the parent class that describes a display
"""


class Display:

    """
    Function to initialize the variables.
    """
    def __init__(self):
        self._type = None
        self._location = None
        self._topic = None
        self._success = None

    """
    Function to get/set to access the attributes of Processor.
    """
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_topic(self):
        return self._topic

    def set_topic(self, topic):
        self.topic = topic

    def get_success(self):
        self.success

    def set_success(self, success):
        self.success = success

    _type = property(get_type, set_type)
    _location = property(get_location, set_location)
    _topic = property(get_topic, set_topic)
    _success = property(get_success, set_success)
