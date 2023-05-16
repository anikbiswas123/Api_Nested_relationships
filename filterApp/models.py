from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    std_name=models.CharField(max_length=100)
    std_Roll=models.CharField(max_length=6)
    std_Dept=models.CharField(max_length=10)
    Std_sub=models.CharField(max_length=20)
    
    def __str__(self):
        return self.std_name

class Purachase(models.Model):
    
    product_name=models.CharField(max_length=100)
    Price=models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.product_name
    
    
