from django.db import models


# Create your models here.
class Singer(models.Model):
    name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    

class Song(models.Model):
    Title=models.CharField(max_length=100)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE,related_name='song')
    Duration=models.IntegerField()
    
    def __str__(self):
        return self.Title
    