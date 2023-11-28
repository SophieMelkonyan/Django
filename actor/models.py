from django.db import models
from movie.models import Movie


def upload_actor_image(instance, filename):
    return f"{instance.first_name}_{instance.last_name}/{filename}"


class Actor(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    average_movie_rate = models.FloatField()
    image = models.ImageField(upload_to=upload_actor_image, null=True, blank=True)

    movie = models.ManyToManyField(Movie, related_name="actor")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "ACTOR"
        verbose_name_plural = "Actors"
        ordering = ["-pk"]
