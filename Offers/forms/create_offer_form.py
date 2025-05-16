from django.forms import ModelForm
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from Offers.models import Offer

class CreateOfferForm(ModelForm):
    # Define a form for creating or editing an Offer model instance
    class Meta:
        model = Offer
        fields = ['price','expiration_date'] # Only include price and expiration_date fields in the form
        widgets ={
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
                }),
            'expiration_date': forms.SelectDateWidget(
                attrs={ 'class':'form-control'},
                years=range(timezone.now().year, timezone.now().year + 50)),
        }

    def clean_expiration_date(self):
        # Custom validation method for expiration_date field
        expiration_date = self.cleaned_data['expiration_date']
        today =timezone.now()
        
        # Ensure expiration date is in the future (not today or past)
        if expiration_date <= today:
            raise ValidationError("Expiration date must be in the future.")
        return expiration_date
