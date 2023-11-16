from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    print(dir(request))
    return render(request, "home.html", {"name": "Hikaru",
                                         "last_name": "Nakamura"})
