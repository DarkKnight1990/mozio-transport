from django.http import response
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

    def test_get_service_provider(self):
        """
        test get API
        """
        provider = ServiceProviderFactory.create()
        url = reverse("service-provider-detail", args=[provider.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(provider.name, response.data["name"])

    def test_delete_service_provider(self):
        """
        test delete API
        """
        provider = ServiceProviderFactory.create()
        url = reverse("service-provider-detail", args=[provider.pk])
        self.assertEqual(ServiceProvider.objects.count(), 1)
        response = self.client.delete(url)
        self.assertEqual(ServiceProvider.objects.count(), 0)
