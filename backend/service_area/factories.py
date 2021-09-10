import factory
import json

from faker import Factory

from django.contrib.gis.geos import GEOSGeometry

from provider.factories import ServiceProviderFactory
from service_area.models import ServiceArea

fake = Factory.create()


def test_area_json():
    return {
        "type": "Polygon",
        "coordinates": [
            [
                [77.57669448852539, 12.985656799993347],
                [77.57360458374022, 12.974616644461282],
                [77.58235931396484, 12.968929100296371],
                [77.60433197021484, 12.970434639348912],
                [77.60244369506836, 12.985991342505251],
                [77.57669448852539, 12.985656799993347],
            ]
        ],
    }


class ServiceAreaFactory(factory.Factory):
    class Meta:
        model = ServiceArea

    name = factory.LazyAttribute(lambda _: fake.city())
    provider = factory.SubFactory(ServiceProviderFactory)
    service_area = factory.LazyAttribute(lambda _: GEOSGeometry(json.dumps(test_area_json())))
    price = 120
