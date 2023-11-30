from django.shortcuts import render, get_object_or_404
from movie.models import Movie
from django.core.paginator import Paginator
from django.db.models import Q


def movies(request):
    all_movies = Movie.objects.filter(is_published=True).order_by("pk")
    if search := request.GET.get("search"):
        all_movies = all_movies.filter(Q(title__startswith=search) | Q(description__icontains=search))
    paginator = Paginator(all_movies, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "movie/movies.html", {"movies": page_obj})


def movie_detail(request, pk: int):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movie/detail.html", {"movie": movie})
