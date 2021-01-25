from .DataStructure import DataStructure
import json

"""
Class used to describe the message to send to retrieve the value of a sensor.
It inherits from the DataStructure class
"""


class SensorData(DataStructure):
    """
    Function to initialize the variables.
    """

    def __init__(self):
        DataStructure.__init__(self)
        self._sensor_name = None
        self._pin_number = None

    """
    Function to return a JSON of SensorData.
    """

    def to_json(self):
        data = DataStructure.to_json(self)
        data["information"]["parameters"] = {
            "pin_number": self._pin_number
        }
        return data

    """
    Function to return a string of JSON of DataStructure.
    """

    def to_string(self):
        return json.dumps(self.to_json(), default=lambda o: o.__dict__,
                          sort_keys=False, indent=4)

    """
    Function to get/set to access the attributes of DataStructure
    """

    def get_pin_number(self):
        return self.pin_number

    def set_pin_number(self, pin_number):
        self.pin_number = pin_number

    _pin_number = property(get_pin_number, set_pin_number)
