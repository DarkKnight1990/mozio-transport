from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


from service_area.models import ServiceArea


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ["id", "name", "provider", "service_area", "price"]
        geo_field = "service_area"
