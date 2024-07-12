from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie

# from .models import className


# Create your views here.
def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "review_list.html", {"movies": movies})


def review_create(request):
    if request.method == "POST":
        # POSTER
        title = request.POST.get("title")
        release_year = request.POST.get("release_year")
        genre = request.POST.get("genre")
        rating = request.POST.get("rating")
        running_time = request.POST.get("running_time")
        review = request.POST.get("review")
        director = request.POST.get("director")
        actor = request.POST.get("actor")
        movie = Movie(
            title=title,
            release_year=release_year,
            genre=genre,
            rating=rating,
            running_time=running_time,
            review=review,
            director=director,
            actor=actor,
        )
        movie.save()
        return redirect("myMovieRiviews:movie_list")
    return render(request, "review_create.html")


# class Movie(models.Model):
#     poster = models.URLField(max_length=300, blank=True)
#     title = models.CharField(max_length=300)
#     release_year = models.IntegerField()
#     genre = models.CharField(max_length=300)
#     rating = models.FloatField()
#     rungging_time = models.IntegerField()
#     review = models.CharField(max_length=1000)
#     director = models.CharField(max_length=300)
#     actor = models.CharField(max_length=300)

# return render(request, 'demos/index.html')
# return render(request, '각 앱/templates 폴더에서의 html 경로', 응답 데이터 )
# HttpResponse(html에 들어갈 내용)
