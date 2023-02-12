from django.db import models


class Artist(models.Model):
    title = models.CharField(verbose_name='название', max_length=90)

    def __str__(self) -> str:
        return self.title


class Album(models.Model):
    artist = models.ForeignKey(
        Artist,
        verbose_name='исполнитель',
        related_name='albums',
        on_delete=models.CASCADE
    )
    year = models.DateField(verbose_name='год выпуска')

    def __str__(self) -> str:
        return str(self.pk)


class Song(models.Model):
    title = models.CharField(verbose_name='название', max_length=90)

    def __str__(self) -> str:
        return self.title


class SequenceNumber(models.Model):
    album = models.ForeignKey(
        Album,
        verbose_name='альбом',
        related_name='sequence_numbers',
        on_delete=models.CASCADE
    )
    song = models.ForeignKey(
        Song,
        verbose_name='песня',
        related_name='sequence_numbers',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ['album', 'song']

    def __str__(self) -> str:
        return str(self.pk)
