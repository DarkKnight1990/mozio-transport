from rest_framework import viewsets

from service_area.models import ServiceArea
from service_area.serializers import ServiceAreaSerializer


class ServiceAreaViewset(viewsets.ModelViewSet):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()
