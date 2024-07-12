from django.db import models


# Create your models here.
class Movie(models.Model):
    poster = models.URLField(max_length=300, blank=True)
    title = models.CharField(max_length=300, default="")
    release_year = models.IntegerField(default=0)
    genre = models.CharField(max_length=300, default="")
    rating = models.FloatField(default=0)
    running_time = models.IntegerField(default=0)
    review = models.CharField(max_length=1000, default="")
    director = models.CharField(max_length=300, default="")
    actor = models.CharField(max_length=300, default="")
