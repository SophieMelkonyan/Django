from django.db import models


def upload_movie_image(instance, filename):
    return f"{instance.title}/{filename}"


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    rate = models.FloatField()
    image = models.ImageField(upload_to=upload_movie_image)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
