from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import JsonResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from decimal import Decimal
from django.contrib.auth.decorators import login_required

from .models import Car, RentalHistory
from .forms import RentalForm

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class ListCars(LoginRequiredMixin, generic.ListView):
    model = Car
    template_name = 'list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        query = Car.objects.filter(availability = True)
        return query
    

class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'detail.html'


class SearchView(generic.TemplateView):
    template_name = 'search.html'


class SearchResultView(generic.ListView):
    model = Car
    template_name = 'search_result.html'
    context_object_name = 'cars'

    def get_queryset(self):
        make = self.request.GET.get("make")
        model = self.request.GET.get("model")
        price = self.request.GET.get("price")
        location = self.request.GET.get("location")
        fuel = self.request.GET.get("fuel")

        queryset = Car.objects.all()

        if make:
            queryset = queryset.filter(make__icontains=make)
        if model:
            queryset = queryset.filter(model__icontains=model)
        if location:
            queryset = queryset.filter(location__icontains=location)
        if fuel:
            queryset = queryset.filter(fuel__icontains=fuel)
        if price:
            try:
                price = Decimal(price)
                queryset = queryset.filter(price__lte=price)
            except (ValueError, TypeError):
                pass

        return queryset


@login_required
def rent_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    user = request.user

    if request.method == 'POST':
        form = RentalForm(request.POST)

        if form.is_valid():
            rental = form.save(commit=False)
            rental.car = car
            rental.user = user
            rental.save()

            car.availability = False
            car.save()

            return redirect('checkout.html', rental_id=rental.id)
        
    else:
        form = RentalForm(initial={'car': car, 'user': user})
    
    return render(request, 'rental_form.html', {'form': form, 'car': car, 'form': form})


def checkout_view(request, rental_id):
    rental = get_object_or_404(RentalHistory, id=rental_id)

    context = {
        'rental': rental
    }

    return render(request, 'checkout.html', context)