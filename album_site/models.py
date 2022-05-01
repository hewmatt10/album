from django.utils import timezone
from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    size = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    description = models.CharField(max_length=2000)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.description

