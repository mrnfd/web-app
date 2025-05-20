from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Seller

class SellerProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateSellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['name',
                  'seller_type',
                  'email',
                  'profile_image_url',
                  'cover_image',
                  'logo',
                  'street',
                  'house_numb',
                  'city',
                  'zip_code',
                  'country',
                  'bio']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_image_url': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'cover_image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'house_numb': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.Select(attrs={'class':'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
        }

        def save(self, *args, **kwargs):
            instance = super(CreateSellerForm, self).save(*args, **kwargs)
            instance.user.save()
            instance.save()
            return instance