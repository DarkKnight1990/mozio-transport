from django.urls import path

from rest_framework import routers

from service_area import views

router = routers.DefaultRouter()
router.register(r"service_area", views.ServiceAreaViewset, "service-area")

urlpatterns = []

urlpatterns += router.urls
