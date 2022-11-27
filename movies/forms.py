from django import forms
from django.core.exceptions import ValidationError

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


class RateMovieForm(forms.ModelForm):
    class Meta:
        model = RateMovie
        fields = ('rate',)
        widgets = {
            'rate': forms.IntegerField()
        }

    def clean(self):
        clean_data = super(RateMovieForm, self).clean()
        if not clean_data.get('rate'):
            raise ValidationError('rate field is empty')
        return clean_data
