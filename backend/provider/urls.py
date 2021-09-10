from django.urls import path

from rest_framework import routers

from provider import views

router = routers.DefaultRouter()
router.register(r"service_provider", views.ServiceProviderViewset, "service-provider")

urlpatterns = router.urls
