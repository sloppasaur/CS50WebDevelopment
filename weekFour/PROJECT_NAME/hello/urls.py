from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name='greet'),
    path("nate", views.nate, name="nate"),
    path("olivia", views.olivia, name="olivia")
]