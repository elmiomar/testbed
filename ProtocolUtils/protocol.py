import abc


class Protocol:
    """class used in IotComponent to regroup every communication protocol
     as a parent class which stands for an Interface"""

    def __init__(self, name):
        self._name = name

    @abc.abstractmethod
    def send_message(self):
        pass

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)
