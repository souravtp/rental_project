from django.urls import path

from . import views

app_name = 'car'

urlpatterns = [
    path('home', views.HomeView.as_view(), name='home'),
    path('list/', views.ListCars.as_view(), name='list'),
    path('details/<int:pk>', views.CarDetailView.as_view(), name='detail')
]
