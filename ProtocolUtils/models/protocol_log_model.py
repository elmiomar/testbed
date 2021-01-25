import datetime

import psycopg2
from django.db import models
from django.db.models import ForeignKey

from CommonTools.commons import exceptions

"""
This class is the model of the protocol log in the database.
A protocol log is linked to a protocol. 
This class is used to log each message exchange through the protocol.
"""


class ProtocolLog(models.Model):
    protocolId: ForeignKey = models.ForeignKey(
        'Protocol',
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)
    message = models.TextField(default='')
    topic = models.TextField(default='')

    def __str__(self):
        return self.name

    """
    Function that returns an object protocol log by an ID.
    """
    @staticmethod
    def get_by_id(protocol_log_id):
        """ Return the object with the given id.

        Args:
            protocol_log_id: Id of protocolLog

        Returns:
            Protocol (obj): Data object with the given id

        """
        try:
            return ProtocolLog.objects.get(pk=str(protocol_log_id))
        except psycopg2.DatabaseError as e:
            raise exceptions.DatabaseError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    """
    Function that returns a list of object protocol log by a protocol.
    """
    @staticmethod
    def get_by_protocol_id(protocol_id):
        """ Return the object with the given id.

        Args:
            protocol_id: Id of the protocol

        Returns:
            Data (obj): ProtocolLog object with the given id

        """
        try:
            return ProtocolLog.objects.filter(protocolId=str(protocol_id))
        except psycopg2.DatabaseError as e:
            raise exceptions.DatabaseError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    """
    Function that returns all protocol log
    """
    @staticmethod
    def get_all():
        """ Get all ProtocolLog.

        Args:


        Returns:

        """
        return ProtocolLog.objects.all()

    """
    Function to create a protocol log in the database.
    """
    @staticmethod
    def create_protocol_log(protocol, message, topic):
        """
        Create a object protocolLog
        :param protocol: Object protocol
        :param message: Message exchanged
        :return: Object ProtocolLog
        """
        protocol_log: ProtocolLog = ProtocolLog(protocolId=protocol, created_date=datetime.datetime.now(), message=message, topic=topic)
        protocol_log.save()
        return protocol_log
