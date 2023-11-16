from django.urls import path
from movie.views import home

urlpatterns = [
    path("first/", home, name="home"),
]
