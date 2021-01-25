from django.db import models
import psycopg2
from CommonTools.commons import exceptions

"""
This class is the model of the sensor in the database.
"""


class Sensor(models.Model):
    name = models.CharField(max_length=255, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    """
    Function that returns an object sensor by a name.
    """
    @staticmethod
    def get_by_sensor_name(sensor_name):
        """ Return the sensor with the given name.

        Args:
            sensor_name: Name of the sensor

        Returns:
            Sensor (obj): Sensor object with the given name

        """
        try:
            return Sensor.objects.get(name=str(sensor_name))
        except psycopg2.DatabaseError as e:
            raise exceptions.DatabaseError(str(e))
        except Exception as ex:
            raise exceptions.ModelError(str(ex))