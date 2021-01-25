import datetime

import psycopg2

from django.db import models
from django.db.models import ForeignKey

from CommonTools.commons import exceptions

"""
This class is the model of the component IOT in the database.
An IOT component is linked to a protocol. 
"""


class IOTComponent(models.Model):
    device_name = models.CharField(max_length=255, default='', unique=True)
    protocol: ForeignKey = models.ForeignKey(
        'ProtocolUtils.Protocol',
        on_delete=models.CASCADE,
    )
    ip_address = models.CharField(max_length=255, default='', unique=True)
    topic = models.CharField(max_length=255, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.device_name

    """
    Function that returns an object IOT component by an ID.
    """
    @staticmethod
    def get_by_id(iot_component_id):
        """ Return the object with the given id.

        Args:
            iot_component_id:

        Returns:
            IOTComponent (obj): IOTComponent object with the given id

        """
        try:
            return IOTComponent.objects.get(pk=str(iot_component_id))
        except psycopg2.DatabaseError as e:
            raise exceptions.DatabaseError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    """
    Function that returns an object IOT component by a device name.
    """
    @staticmethod
    def get_by_device_name(iot_component_device_name):
        """ Return the object with the given device name.

        Args:
            iot_component_device_name: Device name of the IOT Component

        Returns:
            IOTComponent (obj): IOTComponent object with the given device name

        """

        try:
            result = IOTComponent.objects.get(device_name=str(iot_component_device_name))
            return result
        except psycopg2.DatabaseError as e:
            raise exceptions.DatabaseError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))

    """
    Function that returns an object IOT component by an IP address.
    """
    @staticmethod
    def get_by_ip_address(iot_component_ip_address):
        """ Return the object with the given ip address.

        Args:
            iot_component_ip_address: IP address of the IOT component

        Returns:
            IOTComponent (obj): IOTComponent object with the given ip address

        """

        try:
            result = IOTComponent.objects.get(ip_address=str(iot_component_ip_address))
            return result
        except psycopg2.DatabaseError as e:
            print(exceptions.DatabaseError(str(e)))
            return None
        except Exception as ex:
            print(exceptions.ModelError(str(ex)))
            return None

    """
    Function that returns all IOT Components
    """
    @staticmethod
    def get_all():
        """ Get all IOTComponent.

        Args:


        Returns:

        """
        return IOTComponent.objects.all()

    """
    Function to create an IOT Component in the database.
    """
    @staticmethod
    def create_iot_component(device_name, ip_address, protocol):
        """ Create a object IOTComponent

        :param protocol: Protocol use by component
        :param ip_address: IP Address of the device
        :param device_name: Name of device
        :return: IOTComponent
        """
        iot_component: IOTComponent = IOTComponent(device_name=device_name, ip_address=ip_address
                                                   , protocol=protocol, created_date=datetime.datetime.now())
        iot_component.save()
        return iot_component
