from django.db import models
import datetime

from helpers.choices import GenderChoice
from helpers.upload_images import upload_actor_image
from movie.models import Movie


# GENDER_CHOICES = (
#     ("male", "Male"),
#     ("femail", "FEMALE"),
# )


class Actor(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField()
    average_movie_rate = models.FloatField(blank=True, null=True)
    gender = models.CharField(max_length=8, choices=GenderChoice.choices, default="Male")
    image = models.ImageField(upload_to=upload_actor_image, null=True, blank=True)

    movie = models.ManyToManyField(Movie, related_name="actor")

    @property
    def age(self):
        now = datetime.datetime.now().year
        age = now - self.date_of_birth.year
        return age

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_average_movi_rate(self):
        return sum(self.movie.values_list("rate", flat=True)) / len(self.movie.all())

    def save(self, *args, **kwargs):
        if self.movie.exists():
            self.average_movie_rate = sum(self.movie.values_list('rate', flat=True)) / \
                                      self.movie.count()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "ACTOR"
        verbose_name_plural = "Actors"
        ordering = ["-pk"]
