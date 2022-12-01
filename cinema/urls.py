from django.urls import path

from .views import AddMovieView, find_by_id, show_movies

# app_name = "movies"

urlpatterns = [
    path("", show_movies, name="movies"),
    path("more_about/<int:id>/", find_by_id, name="more_about"),
    path("add/", AddMovieView.as_view(), name="add"),
]
