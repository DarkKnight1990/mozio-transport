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

    def test_search_service_area(self):
        test_area = ServiceAreaFactory.create()
        url = reverse("search-area", kwargs={"longitude": "78.7720", "latitude": "22.5126"})
        response = self.client.get(url)
        self.assertEqual(test_area.name, response.data[0]["name"])

    def test_service_area_not_present(self):
        test_area = ServiceAreaFactory.create()
        url = reverse("search-area", kwargs={"longitude": "178.7720", "latitude": "22.5126"})
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)
