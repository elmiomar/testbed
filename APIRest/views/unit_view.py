from rest_framework import viewsets

from APIRest.models.unit_model import Unit
from APIRest.serializers import UnitSerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
