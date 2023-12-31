# Generated by Django 4.2.7 on 2023-11-28 17:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0006_alter_movie_category"),
        ("actor", "0002_rename_actor_actor_movie"),
    ]

    operations = [
        migrations.AlterField(
            model_name="actor",
            name="movie",
            field=models.ManyToManyField(related_name="actor", to="movie.movie"),
        ),
    ]
