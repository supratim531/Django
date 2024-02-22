from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class SingerViewSet(ModelViewSet):
  queryset = Singer.objects.all()
  serializer_class = SingerSerializer

class SongViewSet(ModelViewSet):
  queryset = Song.objects.all()
  serializer_class = SongSerializer
