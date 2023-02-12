from rest_framework import serializers

from .models import Artist, Album, Song, SequenceNumber


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'title')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'artist', 'year')


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'sequence_numbers')


class SequenceNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = SequenceNumber
        fields = ('id', 'album', 'song')
