from TestBed import settings

"""
This class is a class for configuring different information to connect to different protocols.
"""


class Configuration:
    PROTOCOLS = ['MQTT']
    MQTT_CONFIG = {
        'protocol_name': "MQTT",
        'broker_address': "129.6.60.24",
        'certificates_path': settings.CERTIFICATE_PATH_MQTT,
        'broker_port': 8883,
        'broker_user': "cpcc",
        'broker_password': "1qaz!QAZ1qaz"
    }
