from django import forms
from .models import Profile, User
from django.core.exceptions import ValidationError


class UserRegistrationForm(forms.Form):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter().exists()
        if user is None:
            raise ValidationError('This Email Already Exists')
        return email

    def clean(self):
        cd = super().clean()
        pass1 = cd.get('password1')
        pass2 = cd.get('password2')

        if pass1 and pass2 and pass1 != pass2:
            raise ValidationError('Password Must Match')

        return cd


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class EditUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ()
