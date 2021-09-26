from .models import Adventure, Path, RouteTableOne, RouteTableTwo, RouteTableThree, GoodEnding, BadEnding, NeutralEnding
from rest_framework import generics
from .serializers import AdventureSerializer, PathSerializer, RouteTableOneSerializer, RouteTableTwoSerializer, RouteTableThreeSerializer, GoodEndingSerializer, BadEndingSerializer, NeutralEndingSerializer

# Create your views here.
class AdventureList(generics.ListCreateAPIView):
    queryset = Adventure.objects.all()
    serializer_class = AdventureSerializer


class AdventureDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adventure.objects.all()
    serializer_class = AdventureSerializer


class PathList(generics.ListCreateAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer


class PathDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Path.objects.all()
    serializer_class = PathSerializer

class RouteTableOneList(generics.ListCreateAPIView):
    queryset = RouteTableOne.objects.all()
    serializer_class = RouteTableOneSerializer


class RouteTableOneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RouteTableOne.objects.all()
    serializer_class = RouteTableOneSerializer

class RouteTableTwoList(generics.ListCreateAPIView):
    queryset = RouteTableTwo.objects.all()
    serializer_class = RouteTableTwoSerializer


class RouteTableTwoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RouteTableTwo.objects.all()
    serializer_class = RouteTableTwoSerializer

class RouteTableThreeList(generics.ListCreateAPIView):
    queryset = RouteTableThree.objects.all()
    serializer_class = RouteTableThreeSerializer


class RouteTableThreeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RouteTableThree.objects.all()
    serializer_class = RouteTableThreeSerializer

class GoodEndingList(generics.ListCreateAPIView):
    queryset = GoodEnding.objects.all()
    serializer_class =GoodEndingSerializer


class GoodEndingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GoodEnding.objects.all()
    serializer_class = GoodEndingSerializer

class BadEndingList(generics.ListCreateAPIView):
    queryset = BadEnding.objects.all()
    serializer_class =BadEndingSerializer


class BadEndingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BadEnding.objects.all()
    serializer_class = BadEndingSerializer

class NeutralEndingList(generics.ListCreateAPIView):
    queryset = NeutralEnding.objects.all()
    serializer_class = NeutralEndingSerializer


class NeutralEndingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = NeutralEnding.objects.all()
    serializer_class = NeutralEndingSerializer