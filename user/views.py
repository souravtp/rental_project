from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse

from car.models import RentalHistory, Car
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.


class SignUpView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('user:login')


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    form_class = CustomAuthenticationForm


@login_required
def profile_view(request):
    user = request.user
    rental_data = RentalHistory.objects.filter(user=user)

    context = {
        "user": user,
        "rental_data": rental_data
    }

    return render(request, 'profile.html', context)


@login_required
def return_car(request, pk):
    car = Car.objects.get(id=pk)
    user = request.user

    if not car.availability:
        car.availability = True
        car.save()

        return JsonResponse({"message": "Car returned successfully"})

    return redirect(reverse_lazy('user:profile'))
