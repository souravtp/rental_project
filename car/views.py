from django.shortcuts import render
from django.views import generic

from .models import Car

# Create your views here.


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class ListCars(generic.ListView):
    model = Car
    template_name = 'list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        query = Car.objects.filter(availability = True)
        return query
    

class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'detail.html'
    fields = '__all__'
    