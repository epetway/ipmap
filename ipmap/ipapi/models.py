from django.db import models


class IPCoord(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    count = models.IntegerField(default=1)

    class Meta:
        unique_together = ["latitude", "longitude"]
