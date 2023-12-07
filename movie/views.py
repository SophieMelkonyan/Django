from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q

from movie.models import Movie
from movie.forms import SearchForm, MovieForm


def movies(request):
    form = SearchForm()
    all_movies = Movie.objects.order_by("pk")
    if search := request.GET.get("search"):
        is_published = True if request.GET.get("is_published") else False
        category_q = Q(category=request.GET.get("category"))
        year = request.GET.get('year')
        all_movies = all_movies.filter(Q(title__startswith=search) | Q(description__icontains=search)
                                       & Q(is_published=is_published)
                                       & category_q)
        if year:
            all_movies.filter(year=year)
    paginator = Paginator(all_movies, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"movies": page_obj, "form": form,
               "search": request.GET.get("search")}
    return render(request, "movie/movies.html", context)


def movie_detail(request, pk: int):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "movie/detail.html", {"movie": movie})


def add_movie(request):
    form = MovieForm()
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie_instance = form.save(commit=True)
            actors = form.cleaned_data["actor"]
            movie_instance.actor.set(actors)
            movie_instance.save()
            return redirect("movies")
    return render(request, "movie/add_movie.html", {"form": form})
