from django.shortcuts import render
from rest_framework  import viewsets

from .models import *
from .serializers import *

# Create your views here.
class TrackList(viewsets.ModelViewSet):
    queryset=Track.objects.all()
    serializer_class=TrackSerializer
    
class AlbumList(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer    
