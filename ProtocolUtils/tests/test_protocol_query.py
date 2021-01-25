import datetime

from django.test import TestCase
from ProtocolUtils.models import protocol_query
from ProtocolUtils.models.protocol_model import Protocol

"""
This class is a test to test the function to get or save protocol
"""


class ProtocolQueryTest(TestCase):

    def setUp(self):
        super(ProtocolQueryTest, self).setUp()

    def test_save_protocol_object(self):
        protocol = Protocol(name='MQTT',created_date=datetime.datetime.now())
        protocol.save()

    def test_get_protocol_all(self):
        protocol = Protocol(name='MQTT', created_date=datetime.datetime.now())
        protocol.save()

        results = protocol_query.get_all()

        for result in results:
            print(result.name)

    def test_update_protocol_(self):
        protocol = Protocol(name='MQTT', created_date=datetime.datetime.now())
        protocol.save()

        result = protocol_query.get_by_name('MQTT')

        print(result.name)
        result.name = 'MQTT2'
        result.save()
        
        results_update = protocol_query.get_all()

        for result in results_update:
            print(result.name)

