from django.db import models


class IPCoord(models.Model):
    """
    Representation of an IP address location.

    Coordinates are truncated to 4 decimal places of accuracy,
    gives about 11m of accuracy, which is sufficient for high level
    mapping purposes.
    """

    latitude = models.DecimalField(max_digits=9, decimal_places=4)
    longitude = models.DecimalField(max_digits=9, decimal_places=4)
    count = models.IntegerField(default=1)

    class Meta:
        unique_together = ["latitude", "longitude"]
