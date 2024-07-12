from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.shortcuts import get_object_or_404
from .forms import MovieForm

# from .models import className


# Create your views here.
def review_list(request):
    movies = Movie.objects.all()
    print("Movies:", movies)
    return render(request, "review_list.html", {"movies": movies})


def review_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("myMovieRiviews:review_list")
    else:
        form = MovieForm()

    return render(request, "review_create.html", {"form": form})
    # poster = request.FILES.get("poster")
    # title = request.POST.get("title")
    # release_year = request.POST.get("release_year")
    # genre = request.POST.get("genre")
    # rating = request.POST.get("rating")
    # running_time = request.POST.get("running_time")
    # review = request.POST.get("review")
    # director = request.POST.get("director")
    # actor = request.POST.get("actor")
    # movie = Movie(
    #     poster=poster,
    #     title=title,
    #     release_year=release_year,
    #     genre=genre,
    #     rating=rating,
    #     running_time=running_time,
    #     review=review,
    #     director=director,
    #     actor=actor,
    # )
    # movie.save()
    # return redirect("myMovieRiviews:review_list")
    # return render(request, "review_create.html")


def review_detail(request, id):
    movie = Movie.objects.get(id=id)
    context = {"movie": movie}
    return render(request, "review_detail.html", context)


def review_edit(request, id):
    movie = get_object_or_404(Movie, pk=id)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect("myMovieRiviews:review_detail", id=movie.id)
    else:
        form = MovieForm(instance=movie)
    return render(request, "review_create.html", {"form": form, "movie": movie})


def review_delete(request, id):
    movie = get_object_or_404(Movie, id=id)
    movie.delete()
    return redirect("myMovieRiviews:review_list")


# return render(request, 'demos/index.html')
# return render(request, '각 앱/templates 폴더에서의 html 경로', 응답 데이터 )
# HttpResponse(html에 들어갈 내용)
