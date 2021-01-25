import json


class DataStructure():
    """This class is the parent class of every kind of DataStructures"""

    """
    Function to initialize the variables.
    """
    def __init__(self):
        self._type = None
        self._information = None
        self._topic = None
        self._name = None
        self._parameters = None

    """
    Function to return a JSON of DataStructure.
    """
    def to_json(self):
        return {
            "type": self._type,
            "information": {
                "name": self._name,
                "parameters": self._parameters
            },
            "topic": self._topic
        }

    """
    Function to return a string of JSON of DataStructure.
    """
    def to_string(self):
        return json.dumps(self.to_json(), default=lambda o: o.__dict__,
            sort_keys=False, indent=4)

    """
    Function to get/set to access the attributes of DataStructure
    """
    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_information(self):
        return self.information

    def set_information(self, information):
        self.information = information

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, parameters):
        self.parameters = parameters

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_topic(self):
        return self.topic

    def set_topic(self, topic):
        self.topic = topic

    _type = property(get_type, set_type)
    _information = property(get_information, set_information)
    _name = property(get_name, set_name)
    _parameters = property(get_parameters, set_parameters)
    _topic = property(get_topic, set_topic)
