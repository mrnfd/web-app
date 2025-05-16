from django import forms
from django.core.validators import RegexValidator
from datetime import date
from Transactions.models import Transaction, PaymentMethodCreditCard, PaymentMethodBankTransfer, PaymentMethodMortgage, Country

from django import forms
from Transactions.forms.fields import CreditCardField, ExpiryDateField, VerificationValueField

class TransactionForm(forms.ModelForm):
    # Add validators for fields that need specific formats
    contact_SSN = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'placeholder': 'XXX-XX-XXXX'}),
        #validators=[
        #    RegexValidator(
        #        regex=r'^\d{3}-\d{2}-\d{4}$',
        #        message='SSN must be in the format XXX-XX-XXXX',
        #        code='invalid_ssn'
        #    )
        #]
    )
    
    contact_house_number = forms.IntegerField(min_value=1)
    contact_zip = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Transaction
        fields = [
            'contact_name',
            'contact_email',
            'contact_street',
            'contact_house_number',
            'contact_zip',
            'contact_country',
            'contact_SSN',
        ]
        widgets = {
            'contact_country': forms.Select(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        
    #def clean_contact_SSN(self):
    #    # Format the SSN if it's entered without dashes
    #    ssn = self.cleaned_data.get('contact_SSN')
    #    if ssn and len(ssn) == 9 and ssn.isdigit():
    #        ssn = f"{ssn[:3]}-{ssn[3:5]}-{ssn[5:]}"
    #    return ssn

class CreditCardForm(forms.ModelForm):

    contact_name = forms.CharField(max_length=50, required=True)
    card_number = CreditCardField(required=True)
    expiry_date = ExpiryDateField(required=True)
    CVC = VerificationValueField(required=True)

    class Meta:
        model = PaymentMethodCreditCard
        fields = [
            'contact_name','card_number','expiry_date','CVC'
        ]




class BankTransferForm(forms.ModelForm):
    bank_account = forms.CharField(
        max_length=17,
        validators=[
            RegexValidator(
                regex=r'^\d{10,17}$',
                message='Bank account number must be between 10 and 17 digits',
                code='invalid_account_number'
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'Enter account number'})
    )
    
    class Meta:
        model = PaymentMethodBankTransfer
        fields = ['bank_account']


class MortgageForm(forms.ModelForm):
    class Meta:
        model = PaymentMethodMortgage
        fields = ['mortgage_provider']
        widgets = {
            'mortgage_provider': forms.TextInput(attrs={'placeholder': 'Enter mortgage provider name'})
        }


# Combined form for transaction with payment method selection
class PaymentSelectionForm(forms.Form):
    PAYMENT_CHOICES = (
        ('credit_card', 'Credit Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('mortgage', 'Mortgage'),
    )
    
    payment_method = forms.ChoiceField(
        choices=PAYMENT_CHOICES,
        widget=forms.RadioSelect(),
        required=True
    )