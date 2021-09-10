from rest_framework import viewsets

from provider.models import ServiceProvider
from provider.serializers import ServiceProviderSerializer


class ServiceProviderViewset(viewsets.ModelViewSet):
    serializer_class = ServiceProviderSerializer
    queryset = ServiceProvider.objects.all()
