from django.shortcuts import render
from rest_framework import  status

from rest_framework import viewsets

from .models import *
from  .serializers import *
from rest_framework.generics import ListAPIView

# Create your views here.
class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=PurachaseSerializer
    
    def get_queryset(self):
        user=self.request.user
        return Purachase.objects.filter(user=user)
    
