from django.forms import ModelForm
from django import forms

from django import forms
from Listings.models import Listing, PropertyType, ListingStatus, City, ListingImage


class ListingCreateForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['street', 'number', 'zip', 'city',
            'description', 'type', 'price', 'listing_date',
            'numb_of_rooms', 'bath_rooms', 'bed_rooms',
            'size_sqm', 'thumbnail']

        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'zip': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.Select(choices=City.choices, attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'type': forms.Select(choices=PropertyType.choices, attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'listing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'numb_of_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bath_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'bed_rooms': forms.NumberInput(attrs={'class': 'form-control'}),
            'size_sqm': forms.NumberInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
        }


class ListingImageForm(forms.ModelForm):
    class Meta:
        model = ListingImage
        fields = [ 'image_url', 'thumbnail']

        widgets = {
            'listing_id': forms.Select(attrs={'class': 'form-control'}),
            'image_url': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'thumbnail': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }