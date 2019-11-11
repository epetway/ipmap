from rest_framework import serializers

from .models import IPCoord


class IPCoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPCoord
        fields = ["latitude", "longitude", "count"]

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        return [ret["latitude"], ret["longitude"], ret["count"]]
