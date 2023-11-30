from django.urls import path
from movie.views import movies, movie_detail

urlpatterns = [
    path("first/", movies, name="movies"),
    path("movie-detail/<int:pk>/", movie_detail, name="movie_detail"),
]
