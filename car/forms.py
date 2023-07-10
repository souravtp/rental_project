from .models import RentalHistory
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class CustomDateField(forms.DateTimeInput):
    input_type = 'date'


class RentalForm(forms.ModelForm):
    rental_date = forms.DateTimeField(widget=CustomDateField)
    return_date = forms.DateTimeField(widget=CustomDateField)

    class Meta:
        model = RentalHistory
        fields = ['rental_date', 'return_date']


