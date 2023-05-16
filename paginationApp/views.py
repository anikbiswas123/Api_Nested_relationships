from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *
from .mypagination  import *
# Create your views here.

# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=StudentpaginationNumber
    
    
