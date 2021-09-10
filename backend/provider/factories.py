import factory
from faker import Factory

fake = Factory.create()

from provider.models import ServiceProvider


class ServiceProviderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceProvider

    name = factory.LazyAttribute(lambda _: fake.company())
    email = factory.LazyAttribute(lambda _: fake.email())
    phone_number = factory.LazyAttribute(lambda _: fake.phone_number()[:15])
    language = "EN"
    currency = "USD"
