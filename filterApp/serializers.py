from rest_framework  import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class PurachaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purachase
        fields='__all__'
                