from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm, EditUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
# from .models import Relations


class UserRegisterView(View):
    form_class = UserRegistrationForm
    template_name = 'account/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})


    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['user_name'], cd['email'], cd['password1'])
            messages.success(request, 'you are signed up successfully', 'success')
            return redirect('home')
        return render(request, self.template_name, {'form':form})
