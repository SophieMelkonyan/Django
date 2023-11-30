from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from helpers.upload_images import upload_movie_image
from helpers.validators import check_letters


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=150, validators=[check_letters])
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True)
    rate = models.FloatField(blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(10)
    ])
    image = models.ImageField(upload_to=upload_movie_image, null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name="movie")

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def upper_title(self):
        return self.title.upper()

    def __str__(self):
        return f"{self.title}_{self.year}"
