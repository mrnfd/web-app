from django import forms
from .models import Seller

class SellerProfileForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'email', 'contact_number', 'profile_image_url', 'seller_type', 'bio']