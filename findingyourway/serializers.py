from rest_framework import serializers
from .models import Adventure, Path, Route, Ending

class AdventureSerializer(serializers.HyperlinkedModelSerializer):
    paths = serializers.HyperlinkedRelatedField(
        view_name="path_detail", many=True, read_only=True
    )

    class Meta:
        model = Adventure
        fields = ("id", "adventure", "photo_url", "text", "paths")


class PathSerializer(serializers.HyperlinkedModelSerializer):
    routes = serializers.HyperlinkedRelatedField(
        view_name="route_detail", many=True, read_only=True
    )

    class Meta:
        model = Path
        fields = ("id", "path", "photo_url", "text", "routes")

class RouteSerializer(serializers.HyperlinkedModelSerializer):
    endings = serializers.HyperlinkedRelatedField(
    view_name="ending_detail", many=True, read_only=True
    )

    class Meta:
        model = Route
        fields = ("id", "route", "text", "photo_url", "endings" )

class EndingSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Ending
        fields = ("id", "ending", "photo_url", "text",)

