from django.urls import path
from movie.views import movies, movie_detail, add_movie

urlpatterns = [
    path("first/", movies, name="movies"),
    path("movie-detail/<int:pk>/", movie_detail, name="movie_detail"),
    path("add-movie/", add_movie, name="add_movie")
]
