from django.urls import path

from .views import (
    ArtistListCreateAPI,
    ArtistRetriveUpdateDeleteAPI,
    AlbumListCreateAPI,
    AlbumRetriveUpdateDeleteAPI,
    SongListCreateAPI,
    SongRetriveUpdateDeleteAPI,
    SequenceNumberListCreateAPI,
    SequenceNumberRetriveUpdateDeleteAPI,
)


urlpatterns = [
    path('artist/', view=ArtistListCreateAPI.as_view(), name='artist'),
    path(
        'artist/<int:pk>/', 
        view=ArtistRetriveUpdateDeleteAPI.as_view(), 
        name='artist_detail'
    ),
    path('album/', view=AlbumListCreateAPI.as_view(), name='album'),
    path(
        'album/<int:pk>/', 
        view=AlbumRetriveUpdateDeleteAPI.as_view(), 
        name='album_detail'
    ),
    path('song/', view=SongListCreateAPI.as_view(), name='song'),
    path(
        'song/<int:pk>/', 
        view=SongRetriveUpdateDeleteAPI.as_view(), 
        name='song_detail'
    ),
    path(
        'sequence_number/', 
        view=SequenceNumberListCreateAPI.as_view(), 
        name='sequence_number'
    ),
    path(
        'sequence_number/<int:pk>/', 
        view=SequenceNumberRetriveUpdateDeleteAPI.as_view(), 
        name='sequence_number_detail'
    ),
]
