from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import Buyer

# Form to create a new User with username, email, and password fields
class BuyerProfileForm(UserCreationForm):
    class Meta:
        model = User
        # Fields to include in the registration form
        fields = ['username', 'email', 'password1', 'password2']
        
# Form to create or update a Buyer profile (linked to User)
class CreateBuyerForm(ModelForm):
    class Meta:
        model = Buyer
        # Fields to include in the Buyer profile form
        fields = ['name','email', 'contact_number', 'profile_image_url','street','house_numb', 'zip_code', 'country']
        # Custom widgets to style the form inputs with CSS classes
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'profile_image_url': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class':'form-control'}),
            'zip_code': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'}),
        }
        # Custom error messages for validation
        error_messages = {
            'contact_number': {
                'invalid': 'You cannot put text here, only numbers.',
            },
        }

    # Custom validation to ensure contact_number contains only digits
    def clean_contact_number(self):
        contact = self.cleaned_data.get('contact_number')
        if not contact.isdigit():
            raise forms.ValidationError('You cannot put text here, only numbers.')
        return contact

        # Override save method to save both Buyer instance and linked User instance
    def save(self, *args, **kwargs):
        instance = super(CreateBuyerForm, self).save(*args, **kwargs)
        instance.user.save()
        instance.save()
        return instance
