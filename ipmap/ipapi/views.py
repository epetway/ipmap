from rest_framework.generics import ListAPIView


from .models import IPCoord
from .serializers import IPCoordSerializer


class IPCoordListView(ListAPIView):
    queryset = IPCoord.objects.all()[:100]
    serializer_class = IPCoordSerializer
