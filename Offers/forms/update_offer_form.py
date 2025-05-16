from django.forms import ModelForm
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from Offers.models import Offer

class UpdateOfferForm(ModelForm):
    # Form for updating an existing Offer instance
    class Meta:
        model = Offer
        fields = ['price','expiration_date']
        widgets ={
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
                }),
            'expiration_date': forms.SelectDateWidget(
                attrs={ 
                'class':'form-control',
                },
                # Allow selecting years from current year up to 50 years in the future
                years=range(timezone.now().year, timezone.now().year + 50)),
        }
    
    def clean_expiration_date(self):
        # Custom validation for the expiration_date field to ensure it's a future date
        expiration_date = self.cleaned_data['expiration_date']
        today =timezone.now()
        
        # Check if the expiration_date is not in the past or today
        if expiration_date <= today:
            raise ValidationError("Expiration date must be in the future.")
        return expiration_date
