# Generated by Django 3.0.2 on 2020-02-03 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('APIRest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xsensorpropertyunit',
            name='sensorId',
        ),
        migrations.DeleteModel(
            name='Sensor',
        ),
    ]
