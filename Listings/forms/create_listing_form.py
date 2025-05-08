from django.forms import ModelForm
from django import forms

from Listings.models import Listing

class CreateListingForm(ModelForm):
    image = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Listing
        exclude = ['']
        widgets ={
            '': forms.NumberInput(attrs={'class': 'form-control'}),
            '': forms.TextInput(attrs={'class':'form-control'}),
        }