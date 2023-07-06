from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm

# Create your views here.


class SignUpView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user:login')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'

