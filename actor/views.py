from django.shortcuts import render, get_object_or_404
from actor.models import Actor
from django.core.paginator import Paginator



def actor_list(request):
    actors = Actor.objects.all()

    paginator = Paginator(actors, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    cnt = {
        "actors": page_obj
    }
    return render(request, "actor/actor_list.html", context=cnt)


def actor_detail(request, pk: int):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, "actor/detail.html", {"actor": actor})
