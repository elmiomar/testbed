from ProtocolUtils.models import ProtocolLog
from ProtocolUtils.models import protocol_query

"""
Function that returns an object protocol log by an ID.
"""


def get_by_id(protocol_log_id):
    """ Return the object with the given id.

    Args:
        protocol_log_id: Id of protocolLog

    Returns:
        Protocol (obj): Data object with the given id

    """
    return ProtocolLog.get_by_id(protocol_log_id)


"""
Function that returns a list of object protocol log by a id of protocol.
"""


def get_by_protocol_id(protocol_id):
    """ Return the object with the given id.

    Args:
        protocol_id: Id of the protocol

    Returns:
        Data (obj): ProtocolLog object with the given id

    """
    return ProtocolLog.get_by_protocol_id(protocol_id)


"""
Function that returns a list of object protocol log by the name of protocol.
"""


def get_by_protocol_name(protocol_name):
    """ Return the object with the given id.

    Args:
        protocol_name: Id of the protocol

    Returns:
        Data (obj): ProtocolLog object with the given id

    """
    protocol = protocol_query.get_by_name(protocol_name)

    return ProtocolLog.get_by_protocol_id(protocol.Id)


"""
Function that returns all protocol log
"""


def get_all():
    """ Get all ProtocolLog.

    Args:


    Returns:

    """
    return ProtocolLog.get_all()


"""
Function to create an protocol log in the database.
"""


def create_protocol_log(protocol_name, message, topic):
    """
    Create a object protocolLog
    :param topic: Topic of message
    :param protocol_name: Name of protocol
    :param message: Message exchanged
    :return: Object ProtocolLog
    """
    protocol = protocol_query.get_by_name(protocol_name)
    protocol_log = ProtocolLog.create_protocol_log(protocol, message, topic)
    return protocol_log
