from rest_framework.generics import ListAPIView

from django.views.generic import TemplateView

from .models import IPCoord
from .serializers import IPCoordSerializer


class IPCoordListView(ListAPIView):
    queryset = IPCoord.objects.all()
    serializer_class = IPCoordSerializer


class IPCoordMapView(TemplateView):
    template_name = "map.html"
