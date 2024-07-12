from django.urls import path
from .views import *
from django.contrib import admin
from . import views

app_name = "myMovieRiviews"

# path(”자신이 원하는 경로”, view에서 실행되길원하는 함수,URL이름(나중에 template 에서 사용))
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", movie_list, name="index"),
    path("movies/", movie_list, name="movie_list"),
    path("movies/create/", review_create, name="review_create"),
]


# urlpatterns = [
#     path('', post_list), #localhost:8000/posts
#     path('/create', post_create), #localhost:8000/posts/create
#     path('/<int:pk>', post_detail),
#     path('/<int:pk>/update', post_update),
#     path('/<int:pk>/delete', post_delete),
#     path('/<int:pk>/comments/create', comment_create),
# ]
