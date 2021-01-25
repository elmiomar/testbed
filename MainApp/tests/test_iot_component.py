from django.test import TestCase
from MainApp.models import iot_component_query

"""
This class is a test to test the function to create an IOT component
"""


class CreateIOTComponentTest(TestCase):

    def setUp(self):
        super(CreateIOTComponentTest, self).setUp()

    @staticmethod
    def test_create_iot_component():
        test = iot_component_query.create_iot_component('3B+001', '129.6.60.187', 'MQTT')
        #print(test.device_name)
        iot_component1 = iot_component_query.get_by_ip_address('129.6.60.187')
        print(iot_component1.device_name)
