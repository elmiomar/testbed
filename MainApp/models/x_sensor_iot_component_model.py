import psycopg2
from django.db import models
from django.db.models import ForeignKey
from CommonTools.commons import exceptions

"""
This class is the model of the XSensorIOTComponent in the database.
This table connects a sensor and an IOT component.
It allows to know to which sensor the IOT component is linked.
"""


class XSensorIOTComponent(models.Model):
    sensor: ForeignKey = models.ForeignKey(
        'Sensor',
        on_delete=models.CASCADE,
    )
    iot_component: ForeignKey = models.ForeignKey(
        'IOTComponent',
        on_delete=models.CASCADE,
    )
    pin_number = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.pin_number

    """
    Function that returns an object XSensorIOTcomponent by a sensor.
    """
    @staticmethod
    def get_by_sensor(sensor):
        """ Return the object with the given Sensor.

        Args:
            sensor: Object sensor

        Returns:
            XSensorIOTComponent (obj): Return object(s) who correspond with the Sensor

        """
        try:
            return XSensorIOTComponent.objects.filter(sensor=sensor)
        except psycopg2.DatabaseError as e:
            raise exceptions.DatabaseError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))
