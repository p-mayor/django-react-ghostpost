from django.db import models
from django.utils import timezone


class Post(models.Model):
    body = models.CharField(max_length=280)
    is_boast = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)
    time = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.body