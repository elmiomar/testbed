from MainApp.models import IOTComponent
from ProtocolUtils.models import protocol_query

"""
Function that returns an object IOT component by an ID.
"""


def get_by_id(iot_component_id):
    """ Return the object with the given id.

    Args:
        iot_component_id: Id of IOTComponent

    Returns:
        IOTComponent (obj): IOTComponent object with the given id

    """
    return IOTComponent.get_by_id(iot_component_id)


"""
Function that returns an object IOT component by a device name.
"""


def get_by_device_name(device_name):
    """ Return the object with the given device name.

    Args:
        device_name: name of the device

    Returns:
        IOTComponent (obj): IOTComponent object with the device_name

    """

    return IOTComponent.get_by_device_name(device_name)

"""
Function that returns an object IOT component by an IP address.
"""
def get_by_ip_address(ip_address):
    """ Return the object with the ip address.

    Args:
        ip_address: ip address of the device

    Returns:
        IOTComponent (obj): IOTComponent object with the ip_address

    """

    return IOTComponent.get_by_ip_address(ip_address)

"""
Function that returns all IOT Components
"""
def get_all():
    """ Get all IOTComponent.

    Args:


    Returns:

    """
    return IOTComponent.get_all()

"""
Function to create an IOT Component in the database.
"""
def create_iot_component(device_name, ip_address, protocol_name):
    """
    Create a object IOTComponent
    :param device_name:
    :param ip_address:
    :param protocol_name: Name of protocol
    :return: Object IOTComponent
    """
    protocol = protocol_query.get_by_name(protocol_name)
    iot_component = IOTComponent.create_iot_component(device_name, ip_address, protocol)
    return iot_component
