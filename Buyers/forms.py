from django import forms
from .models import Buyer

class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'email', 'contact_number', 'profile_image']