from django.urls import reverse

from rest_framework.test import APITestCase

from .factories import IPCoordFactory


class IPCoordsListViewTestCase(APITestCase):
    def test_get_returns_list_of_ipcoords(self):
        # given a set of existing IPCoords...
        ipcoords = IPCoordFactory.create_batch(2)
        # when a get requests is made to the view...
        response = self.client.get(reverse("ipcoords_list_view"))
        # a json list of coordinate objects is returned...
        expected_response = []
        for ipcoord in ipcoords:
            expected_response.append(
                [f"{ipcoord.latitude:.6f}", f"{ipcoord.longitude:.6f}", ipcoord.count]
            )
        self.assertListEqual(expected_response, response.json())
