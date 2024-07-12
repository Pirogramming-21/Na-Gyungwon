from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            "title",
            "release_year",
            "genre",
            "rating",
            "running_time",
            "review",
            "director",
            "actor",
            "poster",
        )
