from django.shortcuts import render

from .models import *
from .serializers import StudentSerializer

from rest_framework import viewsets
from  rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .Auth import CustomAuthToken

# Create your views here.
class StudentModel_viewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
