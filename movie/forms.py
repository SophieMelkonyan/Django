from django import forms

from actor.models import Actor
from movie.models import Category, Movie


class SearchForm(forms.Form):
    search = forms.CharField(label="search", required=True)
    is_published = forms.BooleanField(label="published", required=False)
    year = forms.ChoiceField(label="production year", required=False,
                             choices=[(None, '---')]+[(i, i) for i in range(1980, 2024)])
    categories = forms.ModelChoiceField(queryset=Category.objects.all())


class MovieForm(forms.ModelForm):
    actor = forms.ModelMultipleChoiceField(queryset=Actor.objects.all())

    class Meta:
        model = Movie
        fields = ("title", "description", "year",
                  "category", "rate", "image", "actor")

    def save(self, commit=True, *args, **kwargs):
        super().save(commit, *args, **kwargs)
