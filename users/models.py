from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=128)
    is_leader = models.BooleanField(default=False)
    picture = models.ImageField(upload_to='media/images/users', default='media/media/images/users/photo_2023-04-19_10-20-05.jpg', blank=True)
