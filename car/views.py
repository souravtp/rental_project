from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from decimal import Decimal

from .models import Car

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
    fields = '__all__'
    

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
        fuel = self.request.GET.get("fuel")

        if price:
            price = Decimal(price)

        return Car.objects.filter(
            Q(make__icontains=make) & Q(model__icontains=model) & Q(price__lte=price) & Q(fuel__icontains=fuel)
        )