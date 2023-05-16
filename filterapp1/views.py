from django.shortcuts import render
from rest_framework  import  status

from rest_framework.generics import ListAPIView
from .models import *
from .serializers import StudentSerializer
from django_filters.rest_framework   import  DjangoFilterBackend

# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields = ['std_city']