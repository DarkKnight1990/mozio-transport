from rest_framework import serializers

from provider.models import ServiceProvider


class ServiceProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ["id", "name", "email", "phone_number", "language", "currency"]
