from django.urls import path
from actor.views import actor_list, actor_detail


urlpatterns = [
    path("all-actors", actor_list, name="actors"),
    path("actor/<int:pk>/", actor_detail, name="actor_detail"),
]
