from django.urls import path
from .views import *
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "myMovieRiviews"

# path(”자신이 원하는 경로”, view에서 실행되길원하는 함수,URL이름(나중에 template 에서 사용))
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", review_list, name="index"),
    path("movies/", review_list, name="review_list"),
    path("movies/create/", review_create, name="review_create"),
    path("movies/details/", review_detail, name="review_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 출처: https://edder773.tistory.com/102 [개발하는 차리의 공부 일기:티스토리]
