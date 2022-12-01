from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView

from . import forms, models
from .forms import AddForm


class AddMovieView(CreateView):

    # model = Books
    form_class = AddForm
    template_name = "add.html"
    success_url = "/"


def show_movies(request):
    movie = models.Movie.objects.all()
    return render(request, "movie_list.html", {"movie": movie})


def find_by_id(request, id):
    movie = get_object_or_404(models.Movie, id=id)
    return render(request, "detail.html", {"movie": movie})
