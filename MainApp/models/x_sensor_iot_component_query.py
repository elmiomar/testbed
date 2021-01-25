from MainApp.models import XSensorIOTComponent, sensor_query

"""
Function that returns an object XSensorIOTcomponent by a name of sensor.
"""
def get_by_sensor_name(sensor_name):
    """ Return the object with the given sensor name.

    Args:
        sensor_name: Name of the sensor

    Returns:
        XSensorIOTComponent (obj): XSensorIOTComponent object with the given sensor name

    """
    sensor = sensor_query.get_by_sensor_name(sensor_name)

    return XSensorIOTComponent.get_by_sensor(sensor.id)