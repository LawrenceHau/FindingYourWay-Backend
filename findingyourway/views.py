from .models import Adventure, Path
from rest_framework import generics
from .serializers import AdventureSerializer, PathSerializer

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