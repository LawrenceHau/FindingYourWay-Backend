from rest_framework import serializers
from .models import Adventure, Path, RouteTableOne

class AdventureSerializer(serializers.HyperlinkedModelSerializer):
    paths = serializers.HyperlinkedRelatedField(
        view_name="path_detail", many=True, read_only=True
    )

    class Meta:
        model = Adventure
        fields = ("id", "adventurename", "photo_url", "adventuretext", "paths")


class PathSerializer(serializers.HyperlinkedModelSerializer):
    adventure = serializers.HyperlinkedRelatedField(
        view_name="adventure_detail", many=False, read_only=True
    )

    class Meta:
        model = Path
        fields = ("adventure", "id", "pathname", "photo_url", "pathtext")

class RouteTableOneSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedRelatedField(
        view_name="path_detail", many=False, read_only=True
    )

    class Meta:
        model = RouteTableOne
        fields = ("id","path", "routename", "photo_url", "routetext")

