from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=255,default='')
    description = models.CharField(max_length=510, default='')
    created_date = models.DateTimeField(auto_now_add=True)
    deleted_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.name