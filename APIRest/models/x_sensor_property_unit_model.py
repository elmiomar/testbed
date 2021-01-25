from django.db import models
from django.db.models import ForeignKey


class XSensorPropertyUnit(models.Model):

    unitId: ForeignKey = models.ForeignKey(
        'Unit',
        on_delete=models.CASCADE,
    )
    propertyId: ForeignKey = models.ForeignKey(
        'Property',
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.unitId, self.propertyId
