from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cite = models.CharField(max_length=500, default='')
    image = models.FileField(default='user_default.jpg', upload_to='user_images')

    def __str__(self):
        return self.user.username + ' Profile'
