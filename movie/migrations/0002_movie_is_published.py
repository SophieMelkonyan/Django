# Generated by Django 4.2.7 on 2023-11-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="is_published",
            field=models.BooleanField(default=True),
        ),
    ]
