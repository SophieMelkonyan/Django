from django.urls import path
from movie.views import movies

urlpatterns = [
    path("first/", movies, name="movies"),
]
