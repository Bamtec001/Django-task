from django.db import models

from turtle import title

class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=50)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    date_released = models.DateField()
    likes = models.IntegerField()

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
