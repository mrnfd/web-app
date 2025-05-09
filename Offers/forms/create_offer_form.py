from django.forms import ModelForm
from django import forms

from Offers.models import Offer

class CreateOfferForm(ModelForm):
    image = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Offer
        exclude = ['listing_id','user_id','offer_status']
        exclude = []
        widgets ={
            'offer_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.TextInput(attrs={'class':'form-control'}),
        }

