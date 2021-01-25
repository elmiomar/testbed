from ProtocolUtils.MQTT.MQTT import Mqtt
from CommonTools.commons import network
from MainApp.models import iot_component_query
import time
import json
from jsonmerge import merge
import sys
from MainApp.sensors.GroveSensors import *
from MainApp.processor import *
from MainApp.display import *

import jsonpickle

"""
This class is a processor class which allows each iot component to subscribe to a given topic according to its IP address.
"""


class MainProcessor:

    def __init__(self):
        pass

    """
    Function to connect the IOT Component to a protocol.
    """
    def connect_protocol(self):
        ip_address = network.get_ip_address()
        iot_component = iot_component_query.get_by_ip_address(ip_address)
        if iot_component is not None:
            getattr(self, 'connect_' + iot_component.protocol.name)(iot_component.topic, iot_component.device_name)
        else:
            print('IOT Component not found')
            """MQTT by default"""
            self.connect_MQTT('listen/test', 'myLaptop')

    """
    Function to connect the IOT component to the MQTT Protocol
    """
    def connect_MQTT(self, topic, device_name):
        protocol = Mqtt()
        protocol.run_mqtt_client(topic, device_name)
        while len(protocol.messageFlow) == 0 or len(protocol.messageFlow) > 0:
            if len(protocol.messageFlow) > 0:
                message_received = json.loads(protocol.messageFlow[0])
                response = self.treat_message(message_received, device_name)
                protocol.send_message(response, message_received['topic'])
                protocol.messageFlow = []

    """
    Function to treat the message received trough the topic subscribe.
    """
    def treat_message(self, message, device_name):
        type = str(message['type'])
        information = message['information']
        message['iot_component'] = device_name
        treatment_return = getattr(self, 'treat_' + type)(information)
        message_return = {**treatment_return, **message}
        return json.dumps(message_return)

    """
    Function to treat the message of type Sensor received trough the topic subscribe.
    """
    def treat_sensor(self, message):
        parameters = str(message['parameters'])
        sensor_name = message['name']
        sensor = eval(str(sensor_name + '(' + parameters + ')'))
        sensor_serialize = json.loads(jsonpickle.encode(sensor))
        return sensor_serialize

    """
    Function to treat the message of type Processor received trough the topic subscribe.
    """
    def treat_processor(self, message):
        processor_name = str(message['name'])
        parameters = str(message['parameters'])
        processor = eval(str(processor_name + '(' + parameters + ')'))
        processor_serialize = json.loads(jsonpickle.encode(processor))
        return processor_serialize

    """
    Function to treat the message of type Display received trough the topic subscribe.
    """
    def treat_display(self, message):
        display_name = str(message['name'])
        parameters = str(message['parameters'])
        display = eval(str(display_name + '(' + parameters + ')'))
        display_serialize = json.loads(jsonpickle.encode(display))
        return display_serialize



