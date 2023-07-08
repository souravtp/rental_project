from .models import RentalHistory
from django import forms
from django.core.exceptions import ValidationError


class CustomDateField(forms.DateInput):
    input_type = 'date'


class RentalForm(forms.ModelForm):
    rental_date = forms.DateTimeField(widget=CustomDateField)
    return_date = forms.DateTimeField(widget=CustomDateField)

    class Meta:
        model = RentalHistory
        fields = ['rental_date', 'return_date']

    def clean(self):
        cleaned_data = super().clean()
        return_date = cleaned_data.get('return_date')
        rented_date = cleaned_data.get('rented_date')

        if rented_date and return_date and return_date < rented_date:
            raise ValidationError('Retun date cannot be earlier than rented date')
