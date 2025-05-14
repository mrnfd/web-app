from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Buyer

class BuyerProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class CreateBuyerForm(ModelForm):
    class Meta:
        model = Buyer
        fields = ['name','email', 'contact_number', 'profile_image_url','street','house_numb', 'zip_code', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_image_url': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class':'form-control'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'}),
        }
        error_messages = {
            'contact_number': {
                'invalid': 'You cannot put text here, only numbers.',
            },
        }

    def clean_contact_number(self):
        contact = self.cleaned_data.get('contact_number')
        if not contact.isdigit():
            raise forms.ValidationError('You cannot put text here, only numbers.')
        return contact 
    
    def save(self, *args, **kwargs):
        instance = super(CreateBuyerForm, self).save(*args, **kwargs)
        instance.user.save()
        instance.save()
        return instance
