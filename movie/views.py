from django.shortcuts import render
from movie.models import Movie
from django.core.paginator import Paginator


def movies(request):
    all_movies = Movie.objects.filter(is_published=True)
    paginator = Paginator(all_movies, 2)
    page_number = request.GET.get("page")
    print(request.GET)
    page_obj = paginator.get_page(page_number)
    return render(request, "movie/movies.html", {"movies": page_obj})
