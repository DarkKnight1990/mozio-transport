from django.test import TestCase
from django.urls import reverse

from rest_framework import test, status

from provider.models import ServiceProvider
from provider.factories import ServiceProviderFactory


class ServiceProviderTests(test.APITestCase):
    def test_create_service_provider(self):
        """
        test if our API creates the service provider
        """
        url = reverse("service-provider-list")
        provider = ServiceProviderFactory.build()
        payload = {
            "name": provider.name,
            "email": provider.email,
            "phone_number": provider.phone_number,
            "language": provider.language,
            "currency": provider.currency,
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ServiceProvider.objects.count(), 1)
        self.assertEqual(ServiceProvider.objects.get().name, provider.name)
