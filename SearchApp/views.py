from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .models import *
from .serializers import StudentSerializer

from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Create your views here.
# class StudentLIst(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     filter_backends=[SearchFilter]
#     # search_fields=['std_city']
#     # search_fields=['^std_name']
#     search_fields=['=std_name','std_city']


class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[OrderingFilter]
    ordering_fields=['std_name','std_city','std_Roll']
    
