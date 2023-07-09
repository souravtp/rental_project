from .models import RentalHistory
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class CustomDateField(forms.DateTimeInput):
    input_type = 'date'


class RentalForm(forms.ModelForm):
    rental_date = forms.DateTimeField(widget=CustomDateField)
    return_date = forms.DateTimeField(widget=CustomDateField)
    rental_amount = forms.DecimalField()

    class Meta:
        model = RentalHistory
        fields = ['rental_date', 'return_date', 'rental_amount']

    def clean(self):
        cleaned_data = super().clean()
        return_date = cleaned_data.get('return_date')
        rental_date = cleaned_data.get('rented_date')

        if rental_date and return_date and return_date < rental_date:
            raise ValidationError('Retun date cannot be earlier than rented date.')

