from rest_framework.generics import ListAPIView


from .models import IPCoord
from .serializers import IPCoordSerializer


class IPCoordListView(ListAPIView):
    """
    Return a list of IP address coordinates, along with
    counts of how many IP addresses are at that specific coordinate.

    get:
        [
            [<lattitude>, <longitude>, <count>],
            ...
        ]
    """

    queryset = IPCoord.objects.all()
    serializer_class = IPCoordSerializer
