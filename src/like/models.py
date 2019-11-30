from django.db import models
from music.models import Song, Album
from user.models import User
# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + '-' + self.song.name
