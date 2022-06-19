from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    ie = models.BooleanField(default=True)
    ns = models.BooleanField(default=True)
    ft = models.BooleanField(default=True)
    pj = models.BooleanField(default=True)