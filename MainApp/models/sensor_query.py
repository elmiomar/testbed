from MainApp.models import Sensor

"""
Function that returns an object sensor by a name.
"""
def get_by_sensor_name(sensor_name):
    """ Return the object with the given name.

    Args:
        sensor_name: Name of the sensor

    Returns:
        Sensor (obj): Sensor object with the given name

    """

    return Sensor.get_by_sensor_name(sensor_name)