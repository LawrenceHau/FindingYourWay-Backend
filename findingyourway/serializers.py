from rest_framework import serializers
from .models import Adventure, Path

class AdventureSerializer(serializers.HyperlinkedModelSerializer):
    adventures = serializers.HyperlinkedRelatedField(
        view_name="path_detail", many=True, read_only=True
    )

    class Meta:
        model = Adventure
        fields = ("id", "adventure", "adventures")


class PathSerializer(serializers.HyperlinkedModelSerializer):
    adventure = serializers.HyperlinkedRelatedField(
        view_name="adventure_detail", many=False, read_only=True
    )

    class Meta:
        model = Path
        fields = ("id", "path", "adventure")