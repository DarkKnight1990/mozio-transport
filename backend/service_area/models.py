from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _

from provider.models import ServiceProvider


class ServiceArea(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Service Area'))
    provider = models.ForeignKey(ServiceProvider, related_name='service_area', on_delete=models.CASCADE)
    service_area = models.PolygonField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self) -> str:
        return self.name
