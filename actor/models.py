from django.db import models
import datetime
from helpers.upload_images import upload_actor_image
from movie.models import Movie


class Actor(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    average_movie_rate = models.FloatField()
    image = models.ImageField(upload_to=upload_actor_image, null=True, blank=True)

    movie = models.ManyToManyField(Movie, related_name="actor")

    @property
    def age(self):
        now = datetime.datetime.now().year
        age = now - self.date_of_birth.year
        return age

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "ACTOR"
        verbose_name_plural = "Actors"
        ordering = ["-pk"]
