from django.db import models

class ServiceProvider(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    language = models.CharField(max_length=10)
    currency = models.CharField(max_length=3)

    def __str__(self) -> str:
        return self.name
