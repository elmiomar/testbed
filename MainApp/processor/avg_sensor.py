from ProtocolUtils.MQTT.MQTT import Mqtt
from .Processor import *
import statistics
from MainApp.models import x_sensor_iot_component_query
from MainApp.data_structure.sensor_data import SensorData

"""
This class is a processor class which calculates the average of the values given by different sensors of the same type.
It inherits from the Processor class
"""


class AVGSensor(Processor):

    """
        Parameters: List with parameters sensor_name
    """
    def __init__(self,parameters):
        Processor.__init__(self)
        """
        We recover the name of the sensors where we want to recover the data
        """
        sensor_name = parameters['sensor_name']
        sensors = x_sensor_iot_component_query.get_by_sensor_name(sensor_name)
        #subscribe topic
        protocol = Mqtt()
        name_topic = 'listen/AVG'
        protocol.run_mqtt_client(name_topic, sensor_name)

        for sensor in sensors:
            #Construct message to send
            message_to_send = SensorData()
            message_to_send.type = "sensor"
            message_to_send.name = sensor.sensor.name
            message_to_send.topic = name_topic
            message_to_send.pin_number = sensor.pin_number
            topic_to_send = sensor.iot_component.topic
            """
            A request is made to each iot component to have the sensor data.
            """
            print(1)
            protocol.send_message(message_to_send.to_string(), topic_to_send)

        time.sleep(2)
        results = protocol.messageFlow
        protocol.messageFlow = []
        list_value = []
        for result in results:
            deserialize = json.loads(result)
            """
            We add the value in an array
            """
            list_value.append(deserialize['value'])

        """
        We calculate the average.
        """
        self.value = statistics.mean(list_value)
        self.timestamp = str(round(time.time(), 3))  # measure Timestamp
