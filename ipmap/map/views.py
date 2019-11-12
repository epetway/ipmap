from django.views.generic import TemplateView


class IPCoordMapView(TemplateView):
    template_name = "map.html"
