from django.urls import path, include
from django.contrib import admin
from .views import *

app_name = "devtools"

urlpatterns = [
    path("", index, name="index"),
    path("tool_list/", tool_list, name="tool_list"),
    path("tool_create", tool_create, name="tool_create"),
    path("tool_detail/<int:pk>/", tool_detail, name="tool_detail"),
    path("tool_delete/<int:pk>/", tool_delete, name="tool_delete"),
    path("tool_update/<int:pk>/", tool_update, name="tool_update"),
]
