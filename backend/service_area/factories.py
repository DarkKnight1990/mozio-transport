import factory
import json

from faker import Factory

from django.contrib.gis.geos import GEOSGeometry

from provider.factories import ServiceProviderFactory
from service_area.models import ServiceArea

fake = Factory.create()

"""
Generated this API response from:
https://geojson.io/#map=2/20.0/0.0
"""


def test_area_json():
    return {
        "type": "Polygon",
        "coordinates": [
            [
                [71.89453125, 25.64152637306577],
                [73.125, 18.93746442964186],
                [84.1552734375, 18.895892559415024],
                [87.36328125, 25.403584973186703],
                [71.89453125, 25.64152637306577],
            ]
        ],
    }


class ServiceAreaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceArea

    name = factory.LazyAttribute(lambda _: fake.city())
    provider = factory.SubFactory(ServiceProviderFactory)
    service_area = factory.LazyAttribute(lambda _: GEOSGeometry(json.dumps(test_area_json())))
    price = 120
