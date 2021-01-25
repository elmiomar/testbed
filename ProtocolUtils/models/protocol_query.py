from ProtocolUtils.models.protocol_model import Protocol

"""
Function that returns an object protocol by an ID.
"""


def get_by_id(protocol_id):
    """ Return protocol object with the given id.

        Parameters:
            protocol_id:

        Returns: protocol object
    """
    return Protocol.get_by_id(protocol_id)

"""
Function that returns an object protocol by a name.
"""


def get_by_name(protocol_name):
    """ Return protocol object with the name protocol.

        Parameters:
            protocol_name:

        Returns: protocol object
    """
    return Protocol.get_by_name(protocol_name)


"""
Function that returns all protocol 
"""


def get_all():
    """ Get all the data if superuser. Raise exception otherwise.

    Parameters:


    Returns: data collection
    """
    return Protocol.get_all()


"""
Function to create a protocol in the database.
"""


def create_protocol(name):
    """

    :param name: name of protocol
    :return: Protocol object
    """
    return Protocol.create_protocol(name)
