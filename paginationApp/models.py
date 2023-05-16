from django.db import models

# Create your models here.
# Create your models here.
class Student(models.Model):
    std_name=models.CharField(max_length=100)
    std_Roll=models.CharField(max_length=6)
    std_Dept=models.CharField(max_length=10)
    Std_sub=models.CharField(max_length=20)
    
    def __str__(self):
        return self.std_name