from django.contrib.gis.geos import Point

from rest_framework import views, viewsets
from rest_framework.response import Response

from service_area.models import ServiceArea
from service_area.serializers import SearchServiceAreaSerializer, ServiceAreaSerializer


class ServiceAreaViewset(viewsets.ModelViewSet):
    serializer_class = ServiceAreaSerializer
    queryset = ServiceArea.objects.all()


class SearchServiceAreaView(views.APIView):
    def get(self, request, longitude, latitude):
        service_areas = ServiceArea.objects.filter(service_area__contains=Point(float(longitude), float(latitude)))
        serializer = SearchServiceAreaSerializer(service_areas, many=True)
        return Response(serializer.data)
