from django.urls import path
from home.views import home, about_us


urlpatterns = [
    path("", home, name="index"),
    path("about-us/", about_us, name="about_us"),
]