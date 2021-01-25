import ssl
import time

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from ProtocolUtils.configuration import Configuration
from ProtocolUtils.protocol import Protocol
from ProtocolUtils.models import protocol_log_query
from ProtocolUtils.models.protocol_model import Protocol as Protocol_o

"""
This class is a class that implements the MQTT protocol.
"""


class Mqtt(Protocol):
    """
    Function to initialize the variables.
    """

    def __init__(self):
        Protocol.__init__(self, Configuration.MQTT_CONFIG['protocol_name'])
        self._broker_address = Configuration.MQTT_CONFIG['broker_address']
        self._certificates_path = Configuration.MQTT_CONFIG['certificates_path']
        self._broker_port = Configuration.MQTT_CONFIG['broker_port']
        self._broker_user = Configuration.MQTT_CONFIG['broker_user']
        self._broker_password = Configuration.MQTT_CONFIG['broker_password']
        self._payload = ""
        self._message_flow = []

    """
    Function to get/set to access the attributes of MQTT
    """

    def _get_broker_address(self):
        return self._broker_address

    def _set_broker_address(self, broker_address):
        self._broker_address = broker_address

    def _get_payload(self):
        return self._payload

    def _set_payload(self, payload):
        self._payload = payload

    def _get_broker_user(self):
        return self._broker_user

    def _set_broker_user(self, broker_user):
        self.broker_user = broker_user

    def _get_broker_password(self):
        return self._broker_password

    def _set_broker_password(self, broker_password):
        self._broker_password = broker_password

    def _get_broker_port(self):
        return self._broker_port

    def _set_broker_port(self, broker_port):
        self._broker_port = broker_port

    def _get_certificates_path(self):
        return self._certificates_path

    def _set_certificates_path(self, certificates_path):
        self._certificates_path = certificates_path

    def _get_message_flow(self):
        return self._message_flow

    def _set_message_flow(self, message_flow):
        self._message_flow = message_flow

    """
    Function used to send messages.
    message : Message to send
    topic : Topic where the message is send
    """

    def send_message(self, message, topic):
        authentication = {'username': self.broker_user,
                          'password': self.broker_password}  # setting Authentication informations
        TLS = {'ca_certs': self.certificates_path}  # security configuration
        publish.single(
            topic, message, port=self.broker_port, hostname=self.broker_address,  # send the message
            auth=authentication, protocol=mqtt.MQTTv31, tls=TLS
        )

    """
    Callback function triggered each time a client connects to the broker.
    return_code : Return code to know the error of connection
    """

    def on_connect(client, userdata, flags,
                   return_code):
        if return_code == 0:
            client.connected_flag = True  # set flag
        else:
            switcher = {
                1: 'incorrect protocol version',
                2: 'invalid client identifier',
                3: 'server unavailable',
                4: 'bad username or password',
                5: 'not authorised'
            }
            print(switcher.get("Connection refused – " + return_code, "Connection refused"))
            client.bad_connection_flag = True  # create flag in class

    """
    Callback function triggered each time a client gets disconnected from the broker.
    return_code : Return code to know the error of disconnection
    """

    def on_disconnect(client, userdata, return_code):

        switcher = {
            1: 'incorrect protocol version',
            2: 'invalid client identifier',
            3: 'server unavailable',
            4: 'bad username or password',
            5: 'not authorised'
        }
        print(switcher.get("Connection refused – " + return_code, "Connection refused"))
        client.connected_flag = False

    """
    This function is triggered each time a message arrives on the broker. 
    message : Message received, decoded, logged and added in an array.
    """

    def message_callback(self, client, userdata, message):
        payload = message.payload.decode("utf-8")
        topic = str(message.topic)
        protocol_log_query.create_protocol_log(self.name, payload, topic)
        self.payload = payload  # store the payload into the class
        self.messageFlow.append(payload)
        return payload

    def on_log(mqttc, obj, level, string):
        print(string)

    """
    This function create new client instance. It subscribes on a topic and wait a message
    topic: The topic where the new instance subscribes.
    name: The name of the new instance, if it is null, a name random is given.
    """

    def run_mqtt_client(self, topic, name):
        client = mqtt.Client("", True, None, mqtt.MQTTv31)

        client.tls_set(ca_certs=self.certificates_path,
                       tls_version=ssl.PROTOCOL_TLSv1_2)  # give the client certificates in order to connect on the broker
        client.username_pw_set(self.broker_user, password=self.broker_password)  # give client credentials
        client.connected_flag = False
        client.bad_connection_flag = False
        client.on_message = self.message_callback  # bind call-back functions
        client.on_connect = self.on_connect  # bind call-back functions

        client.on_disconnect = self.on_disconnect  # bind call-back functions
        client.on_log = self.on_log
        client.connect(self.broker_address, self.broker_port,
                       60)  # 10 seconds is the time without response before trigger disconnecting function
        client.loop_start()
        client.subscribe(topic)  # client subscribe to the given topic from the MQTT broker
        time.sleep(1)

    certificates_path = property(_get_certificates_path, _set_certificates_path)  # Secured getters and setters
    broker_port = property(_get_broker_port, _set_broker_port)
    broker_password = property(_get_broker_password, _set_broker_password)
    broker_user = property(_get_broker_user, _set_broker_user)
    broker_address = property(_get_broker_address, _set_broker_address)
    payload = property(_get_payload, _set_payload)
    messageFlow = property(_get_message_flow, _set_message_flow)
