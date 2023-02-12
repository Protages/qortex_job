from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)

from .models import Artist, Album, Song, SequenceNumber
from . import serializers


class ArtistListCreateAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Artist.objects.all()
    serializer_class = serializers.ArtistSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    
class ArtistRetriveUpdateDeleteAPI(
        RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
    ):
    queryset = Artist.objects.all()
    serializer_class = serializers.ArtistSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AlbumListCreateAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    
class AlbumRetriveUpdateDeleteAPI(
        RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
    ):
    queryset = Album.objects.all()
    serializer_class = serializers.AlbumSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SongListCreateAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    
class SongRetriveUpdateDeleteAPI(
        RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
    ):
    queryset = Song.objects.all()
    serializer_class = serializers.SongSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SequenceNumberListCreateAPI(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = SequenceNumber.objects.all()
    serializer_class = serializers.SequenceNumberSerializer

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    
class SequenceNumberRetriveUpdateDeleteAPI(
        RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
    ):
    queryset = SequenceNumber.objects.all()
    serializer_class = serializers.SequenceNumberSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
