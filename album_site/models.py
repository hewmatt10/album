from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    creation_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.description

