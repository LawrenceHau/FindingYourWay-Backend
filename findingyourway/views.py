from .models import Adventure, Path, Route, Ending
from rest_framework import generics
from .serializers import AdventureSerializer, PathSerializer, RouteSerializer, RouteSerializer, RouteSerializer, EndingSerializer

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

class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

class EndingList(generics.ListCreateAPIView):
    queryset = Ending.objects.all()
    serializer_class = EndingSerializer


class EndingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ending.objects.all()
    serializer_class = EndingSerializer

