from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


from service_area.models import ServiceArea


"""
Using the rest_framework.gis module:
followed this link:

https://github.com/openwisp/django-rest-framework-gis
"""


class ServiceAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ServiceArea
        fields = ["id", "name", "provider", "service_area", "price"]
        geo_field = "service_area"


class SearchServiceAreaSerializer(serializers.ModelSerializer):
    provider = serializers.StringRelatedField()

    class Meta:
        model = ServiceArea
        fields = ("name", "provider", "price")
