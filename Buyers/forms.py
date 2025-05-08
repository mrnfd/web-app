from django import forms
from .models import Buyer

class BuyerProfileForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['name', 'email', 'contact_number', 'profile_image']
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