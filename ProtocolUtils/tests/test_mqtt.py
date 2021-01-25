import time

from django.test import TestCase

from ProtocolUtils.MQTT.MQTT import Mqtt
from ProtocolUtils.models import protocol_query, protocol_log_query
from ProtocolUtils.models.protocol_model import Protocol

"""
This class is a test to test the function to test a connection
"""


class MQTTTest(TestCase):

    def setUp(self):
        self.protocol = Mqtt()


    def test_connection(self):
        protocol_query.create_protocol('MQTT')

        self.protocol.run_mqtt_client('testTopic', 'nameClientMQTT')

        self.protocol.send_message("{messageOfSendMessage}", "testTopic")
        time.sleep(5)

        results = protocol_log_query.get_all()
        for result in results:
            print(result.message)
            print(result.protocolId)

        print('success')
