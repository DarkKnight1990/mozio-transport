import json

from django.urls import reverse

from rest_framework import test, status

from provider.factories import ServiceProviderFactory
from service_area.factories import test_area_json, ServiceAreaFactory
from service_area.models import ServiceArea


class ServiceAreaTests(test.APITestCase):
    def test_service_area_create(self):
        provider = ServiceProviderFactory.create()
        payload = {"name": "Test-Area", "service_area": test_area_json(), "price": 200.75, "provider": provider.id}
        url = reverse("service-area-list")
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceArea.objects.count(), 1)
        self.assertEqual(ServiceArea.objects.get().name, payload["name"])
