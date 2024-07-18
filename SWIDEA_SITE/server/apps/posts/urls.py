from django.urls import path, include
from django.contrib import admin
from .views import *

app_name = "posts"

# urlpatterns = [path("admin/", admin.site.urls), path("", include("apps.post.urls"))]


urlpatterns = [
    path("", index, name="index"),
    path("", list, name="list"),
    path("create/", create, name="create"),
    path("detail/<int:pk>/", detail, name="detail"),
    path("delete/<int:pk>/", delete, name="delete"),
    path("update/<int:pk>/", update, name="update"),
    path("list/<str:order_by>/", order, name="order"),
    path("posts/<int:pk>/mark/", mark, name="mark"),
    path("<int:pk>/update-interest/", update_interest, name="update_interest"),
]
