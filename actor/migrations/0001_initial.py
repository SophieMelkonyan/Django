# Generated by Django 4.2.7 on 2023-11-28 17:39

import actor.models
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("movie", "0005_movie_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Actor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=250)),
                ("last_name", models.CharField(max_length=250)),
                ("date_of_birth", models.DateField()),
                ("average_movie_rate", models.FloatField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=actor.models.upload_actor_image
                    ),
                ),
                ("actor", models.ManyToManyField(to="movie.movie")),
            ],
            options={
                "verbose_name": "ACTOR",
                "verbose_name_plural": "Actors",
                "ordering": ["-pk"],
            },
        ),
    ]