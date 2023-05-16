from django.shortcuts import render

from rest_framework import viewsets

from .models import  *
from .serializers import *


# Create your views here.
class SongList(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer
    

class SingerList(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SinngerSerializer
        
    
