from django.db import models
from django.utils import timezone


class Post(models.Model):
    post_text = models.CharField(max_length=280)
    boast = models.BooleanField(default=True)
    votes = models.IntegerField(default=0)
    upordown = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.post_text