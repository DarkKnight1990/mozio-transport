from django.urls import re_path

from rest_framework import routers

from service_area import views

router = routers.DefaultRouter()
router.register(r"service_area", views.ServiceAreaViewset, "service-area")

urlpatterns = [
    re_path(
        r"^search/(?P<longitude>(\-?\d+(\.\d+)?))/(?P<latitude>(\-?\d+(\.\d+)?))/$",
        views.SearchServiceAreaView.as_view(),
        name="search-area",
    )
]

urlpatterns += router.urls
