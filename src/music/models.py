from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default=False)
    image = models.FileField(default='album_default.jpg', upload_to='album_images')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)

    def __str__(self):
        return self.title + ' - ' + self.artist

    def get_absolute_url(self):
        return reverse('music:album-detail', kwargs={'pk': self.pk})


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    music = models.FileField(upload_to='music')
    genre = models.CharField(max_length=200)
    is_liked = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + '.mp3'

    # def get_absolute_url(self):
    #     return reverse('music:album-detail', kwargs={'pk': self.album.pk})
