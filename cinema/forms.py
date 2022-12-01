from django import forms

from .models import Movie


class AddForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ("title", "description", "image")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }
