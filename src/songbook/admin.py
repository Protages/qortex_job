from django.contrib import admin

from .models import Artist, Album, Song, SequenceNumber


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'artist', 'year')


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(SequenceNumber)
class SequenceNumberAdmin(admin.ModelAdmin):
    list_display = ('id', 'album', 'song')
