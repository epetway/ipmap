from django.urls import path

from . import views

urlpatterns = [
    path("", views.IPCoordMapView.as_view(), name="ip_map_view"),
]
