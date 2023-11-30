from django.contrib import admin

from actor.models import Actor


class ActorAdmin(admin.ModelAdmin):
    fields = ["first_name", "last_name",
              "date_of_birth", "average_movie_rate",
              "image", "age", "movie"]
    readonly_fields = ("age",)


admin.site.register(Actor, ActorAdmin)
