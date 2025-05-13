from django.forms import ModelForm
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError

from Offers.models import Offer

class UpdateOfferForm(ModelForm):
    class Meta:
        model = Offer
        #exclude = ['id','property_listing_id','buyer_id','status','submission_date']
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
                years=range(timezone.now().year, timezone.now().year + 50)),
        }
    
    def clean_expiration_date(self):
        expiration_date = self.cleaned_data['expiration_date']
        today =timezone.now()
        
        # Validate that expiration_date is after today
        if expiration_date <= today:
            raise ValidationError("Expiration date must be in the future.")
        return expiration_date
