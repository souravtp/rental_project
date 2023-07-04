from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user:login')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('car:list')
