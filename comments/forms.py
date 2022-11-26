from django.core.exceptions import ValidationError
from django import forms

from comments.models import MovieComment


class CommentForm(forms.ModelForm):

    class Meta:
        model = MovieComment
        fields = ('comment_body',)
        widgets = {
            'comment_body': forms.Textarea(attrs={'class': 'form-control'})
        }

    def clean(self):
        clean_data = super(CommentForm, self).clean()
        if not clean_data.get('comment_body'):
            raise ValidationError('comment ody is empty')

        return clean_data