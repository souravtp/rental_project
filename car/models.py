from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.


class Car(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=150)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=50)
    fuel = models.CharField(max_length=50)
    registration_number = models.CharField(max_length=20)
    stars = models.DecimalField(max_digits=3, decimal_places=2, validators=[MaxValueValidator(5.00)])
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.make