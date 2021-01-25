from rest_framework import serializers
from APIRest.models.unit_model import Unit


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name', 'description']
