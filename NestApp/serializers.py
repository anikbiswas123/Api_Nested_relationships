
from rest_framework import serializers
from .models import *


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Track
        fields=['id','album','order','title','duration']

class AlbumSerializer(serializers.ModelSerializer):
    #tracks = serializers.StringRelatedField(many=True)
    # tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # tracks = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='track-detail'
    # )
    # tracks = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    #  )
    # track_listing = serializers.HyperlinkedIdentityField(view_name='track-list')
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model=Album
        fields=['id','album_name','artist','tracks']
        
        # def create(self, validated_data):
        #       tracks_data = validated_data.pop('tracks')
        #       album = Album.objects.create(**validated_data)
        #       for track_data in tracks_data:
        #         Track.objects.create(album=album, **track_data)
        #         return album        