from django.test import TestCase
from django.urls import reverse


class IPCoordMapView(TestCase):
    def test_ipmap_view_returns_200(self):
        response = self.client.get(reverse("ip_map_view"))
        self.assertEqual(response.status_code, 200)
