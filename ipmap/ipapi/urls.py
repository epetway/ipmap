from django.urls import path

from . import views

urlpatterns = [
    path("ipcoords/", views.IPCoordListView.as_view(), name="ipcoords_list_view"),
]
