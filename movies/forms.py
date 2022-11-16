from django import forms
from .models import *


class MovieForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MovieForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Movie
        fields = ('title', 'description', 'imdb_score', 'release_date', 'avatar')
