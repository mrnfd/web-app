from django.forms import ModelForm
from django import forms
from django.forms import inlineformset_factory

from Listings.models import Listing, ListingImage

class PropertyListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'price', 'description', 'available_from']
        widgets = {
            'available_from': forms.DateInput(attrs={'type': 'date'}),
        }

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = ListingImage
        fields = ['image_url', 'is_primary']

# Create a formset for handling multiple images at once

PropertyImageFormSet = inlineformset_factory(
    Listing, ListingImage,
    form=PropertyImageForm,
    extra=3,  # Number of empty forms to display
    can_delete=True
)