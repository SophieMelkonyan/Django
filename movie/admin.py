from django.contrib import admin

from movie.models import Movie, Category

admin.site.register(Movie)
admin.site.register(Category)
