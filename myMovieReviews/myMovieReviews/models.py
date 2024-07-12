from django.db import models
from django import forms


# Create your models here.
class Movie(models.Model):
    genre_choices = [
        # ('DB저장', 'display')
        ("action", "액션"),
        ("animation", "애니메이션"),
        ("comedy", "코미디"),
        ("documentary", "다큐멘터리"),
        ("drama", "드라마"),
        ("fantasy", "판타지"),
        ("horror", "호러"),
        ("musical", "뮤지컬"),
        ("romance", "로맨스"),
        ("sf", "SF"),
        ("thriller", "스릴러"),
        ("historical", "사극"),
    ]
    # https://ugaemi.com/django/Django-choices-field/
    poster = models.ImageField(upload_to="", blank=True, default="default.jpg")
    title = models.CharField(max_length=300, default="")
    release_year = models.IntegerField(default=0)
    genre = models.CharField(max_length=100, choices=genre_choices, default="")
    rating = models.FloatField(default=0)
    running_time = models.IntegerField(default=0)
    review = models.CharField(max_length=1000, default="")
    director = models.CharField(max_length=300, default="")
    actor = models.CharField(max_length=300, default="")
