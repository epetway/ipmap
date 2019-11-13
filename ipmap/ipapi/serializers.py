from rest_framework import serializers

from .models import IPCoord


class IPCoordSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPCoord
        fields = ["latitude", "longitude", "count"]

    def to_representation(self, instance):
        # Returning a pure array to reduce response size.
        ret = super().to_representation(instance)
        return [ret["latitude"], ret["longitude"], ret["count"]]
