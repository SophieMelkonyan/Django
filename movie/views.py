from django.shortcuts import render
# from django.http import HttpResponse
from movie.models import Movie


def movies(request):
    all_movies = Movie.objects.filter(is_published=True)
    return render(request, "movie/movies.html", {"movies": all_movies})
