from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = (
            "poster",
            "title",
            "release_year",
            "genre",
            "rating",
            "running_time",
            "review",
            "director",
            "actor",
        )
        widgets = {
            "poster": forms.ClearableFileInput(attrs={"class": "review__form"}),
            "title": forms.TextInput(
                attrs={"class": "review__form", "placeholder": "제목"}
            ),
            "release_year": forms.NumberInput(
                attrs={"class": "review__form", "placeholder": "개봉년도"}
            ),
            "genre": forms.Select(attrs={"class": "review__form"}),
            "rating": forms.NumberInput(
                attrs={"class": "review__form", "placeholder": "별점"}
            ),
            "running_time": forms.NumberInput(
                attrs={"class": "review__form", "placeholder": "러닝타임"}
            ),
            "review": forms.Textarea(
                attrs={"class": "review__form", "placeholder": "리뷰"}
            ),
            "director": forms.TextInput(
                attrs={"class": "review__form", "placeholder": "감독"}
            ),
            "actor": forms.TextInput(
                attrs={"class": "review__form", "placeholder": "배우"}
            ),
        }


# https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
# class CommentForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "special"}))
#     url = forms.URLField()
#     comment = forms.CharField(widget=forms.TextInput(attrs={"size": "40"}))
