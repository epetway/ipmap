from rest_framework.views import APIView
from rest_framework.response import Response

from .models import IPCoord


class IPCoordListView(APIView):
    """
    Return a list of IP address coordinates, along with
    counts of how many IP addresses are at that specific coordinate.

    get:
        [
            [<latitude>, <longitude>, <count>],
            ...
        ]
    """

    def get(self, request):
        data = [
            [str(ipcoord.latitude), str(ipcoord.longitude), ipcoord.count]
            for ipcoord in IPCoord.objects.all()
        ]
        return Response(data)
