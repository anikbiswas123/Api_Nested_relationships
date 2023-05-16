

from rest_framework  import  serializers

from  .models  import *

class SongSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Song
        fields=['id','Title','singer','Duration',] 

class SinngerSerializer(serializers.ModelSerializer):
    tracks = SongSerializer(many=True)
    class  Meta:
        model=Singer
        fields=['id','name','Gender','tracks']

