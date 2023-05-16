from django.db import models

# Create your models here.
class Student(models.Model):
    std_name=models.CharField(max_length=100)
    std_Roll=models.CharField(max_length=10)
    std_city=models.CharField(max_length=30)
    
    def __str__(self):
        return self.std_name
    