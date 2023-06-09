
from rest_framework import serializers

from .models import Singer,Song



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'


class SingerSerializer(serializers.ModelSerializer):
    # song=serializers.StringRelatedField(many=True,read_only=True)
    # song=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # song=serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')
    song=serializers.HyperlinkedRelatedField(many=True,read_only=True,slug_field='song-list')
    class Meta:
        model=Singer
        fields=['id','name','Gender','song']        