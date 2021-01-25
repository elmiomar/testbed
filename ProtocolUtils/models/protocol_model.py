import datetime

import psycopg2

from django.db import models
from CommonTools.commons import exceptions

"""
This class is the model of the protocol in the database.
This class is used to register each protocol in the database.
"""


class Protocol(models.Model):
    name = models.CharField(max_length=255, default='', unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)



    def __str__(self):
        return self.name

    """
    Function that returns an object protocol by an ID.
    """
    @staticmethod
    def get_by_id(protocol_id):
        """ Return the object with the given id.

        Args:
            protocol_id:

        Returns:
            Protocol (obj): Data object with the given id

        """
        try:
            return Protocol.objects.get(pk=str(protocol_id))
        except psycopg2.DatabaseError as e:
            raise exceptions.DatabaseError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    """
    Function that returns an object protocol by a name .
    """
    @staticmethod
    def get_by_name(protocol_name):
        """ Return the object with the given id.

        Args:
            protocol_name:

        Returns:
            Data (obj): Data object with the given id

        """

        try:
            result = Protocol.objects.get(name=str(protocol_name))
            return result
        except psycopg2.DatabaseError as e:
            raise exceptions.DatabaseError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    """
    Function that returns all protocol 
    """
    @staticmethod
    def get_all():
        """ Get all protocol.

        Args:


        Returns:

        """
        return Protocol.objects.all()

    """
    Function to create a protocol in the database.
    """
    @staticmethod
    def create_protocol(name):
        """ Create a object protocol

        :param name: Name of protocol
        :return: Protocol
        """
        protocol: Protocol = Protocol(name=name, created_date=datetime.datetime.now())
        protocol.save()
        return protocol
