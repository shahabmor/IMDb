from django import forms
from .models import *


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'description', 'imdb_score', 'release_date', 'avatar', 'genres', 'crew')
