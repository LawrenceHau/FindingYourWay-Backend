from rest_framework import serializers
from .models import Adventure, Path, RouteTableOne, RouteTableTwo, RouteTableThree, GoodEnding, BadEnding, NeutralEnding

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
    routetableone = serializers.HyperlinkedRelatedField(
        view_name="routetableone_detail", many=True, read_only=True
    )
    routetabletwo = serializers.HyperlinkedRelatedField(
        view_name="routetabletwo_detail", many=True, read_only=True
    )
    routetablethree = serializers.HyperlinkedRelatedField(
        view_name="routetablethree_detail", many=True, read_only=True
    )

    class Meta:
        model = Path
        fields = ("adventure", "id", "pathname", "photo_url", "pathtext", "routetableone", "routetabletwo", "routetablethree")

class RouteTableOneSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedRelatedField(
        view_name="path_detail", many=False, read_only=True
    )
    goodending = serializers.HyperlinkedRelatedField(
    view_name="goodending_detail", many=True, read_only=True
    )



    class Meta:
        model = RouteTableOne
        fields = ("id","path", "routename", "photo_url", "routetext", "goodending")

class RouteTableTwoSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedRelatedField(
        view_name="path_detail", many=False, read_only=True
    )
    badending = serializers.HyperlinkedRelatedField(
        view_name="badending_detail", many=True, read_only=True
    )

    class Meta:
        model = RouteTableTwo
        fields = ("id","path", "routename", "photo_url", "routetext", "badending",)

class RouteTableThreeSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedRelatedField(
        view_name="path_detail", many=False, read_only=True
    )
    neutralending = serializers.HyperlinkedRelatedField(
    view_name="neutralending_detail", many=True, read_only=True
    )

    class Meta:
        model = RouteTableThree
        fields = ("id","path", "routename", "photo_url", "routetext", "neutralending")

class GoodEndingSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedRelatedField(
    view_name="path_detail", many=False, read_only=True
    )

    class Meta:
        model = GoodEnding
        fields = ("id", "endingname", "photo_url", "endingtext", "path")

class BadEndingSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedRelatedField(
    view_name="path_detail", many=False, read_only=True
    )

    class Meta:
        model = BadEnding
        fields = ("id", "endingname", "photo_url", "endingtext", "path")

class NeutralEndingSerializer(serializers.HyperlinkedModelSerializer):
    path = serializers.HyperlinkedRelatedField(
    view_name="path_detail", many=False, read_only=True
    )

    class Meta:
        model = NeutralEnding
        fields = ("id", "endingname", "photo_url", "endingtext", "path")