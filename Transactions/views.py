from Transactions.forms.finalization_form import TransactionForm, CreditCardForm, BankTransferForm, MortgageForm
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from Listings.models import Listing
from Buyers.models import Buyer
from Offers.models import Offer
from Transactions.models import Transaction
import datetime

@login_required
def finalization(request, offer_id):

    offer = get_object_or_404(Offer, id=offer_id)

    if request.method == "POST":

        try:
            transaction = Transaction.objects.get(offer=offer)
            form = TransactionForm(request.POST,instance=transaction)
        except Transaction.DoesNotExist:
            form = TransactionForm(request.POST)
        
        if form.is_valid():
           
            transaction = form.save(commit=False)
            transaction.offer_id = offer.id
            transaction.save()  # Save to generate an ID
            
            
            # Get the payment option from the form data
            payment_option = request.POST.get('payment_option')
            
            
            # Redirect based on the payment option
            if payment_option == 'credit_card':
                return redirect('finalization_credit', transaction_id=transaction.id)
            elif payment_option == 'bank_transfer':
                return redirect('finalization_bank', transaction_id=transaction.id)
            elif payment_option == 'mortgage':
                return redirect('finalization_mortgage', transaction_id=transaction.id)
            
            else:
                messages.error(request, 'Invalid payment option selected.')
                return render(request, 'transactions/finalize_offer.html', {
                    "form": form, 
                    'offer': offer_id,
                    'transaction_id': transaction.id
                })
        else:
            print("Form is invalid")  # Debug print
            print(f"Form errors: {form.errors}")  # Debug print to see validation errors
            messages.error(request, 'Please correct the errors in the form.')
            return render(request, 'transactions/finalize_offer.html', {
                "form": form, 
                'offer': offer_id,
                'transaction_id': None
            })
    else:

        try:
            transaction = Transaction.objects.get(offer=offer)
            form = TransactionForm(instance=transaction)
        except Transaction.DoesNotExist:
            form = TransactionForm(initial={
            'contact_email': request.user.email,
            'contact_name': request.user.buyer.name,
            'contact_street': request.user.buyer.street,
            'contact_house_number': request.user.buyer.house_numb,
            'contact_zip': request.user.buyer.zip_code,
            'contact_country': request.user.buyer.country,
            }
        )
        return render(request, 'transactions/finalize_offer.html', {
            'form': form,
            'offer': offer_id,
            'transaction_id': None,
        })

@login_required
def finalization_credit(request,transaction_id):
    transaction=get_object_or_404(Transaction,id=transaction_id)
    if request.method == "POST":
        
        form = CreditCardForm(request.POST)

        if form.is_valid():

            payment_info = form.save(commit=False)
            payment_info.transaction_id = transaction
            
            #payment_info.save()
            return render(request,'transactions/finalization_credit.html',{
                'form':form,
                'transaction':transaction,
                })
        
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            
            # Rendera síðu ánþess að missa upplýsingar
            return render(request,'transactions/finalization_credit.html',{"form":form,
                                                                           'transaction':transaction,})
    else:
    
        return render(request, 'transactions/finalization_credit.html',{
            'form': CreditCardForm(),
            'transaction':transaction,
        })
   

@login_required
def finalization_bank(request):
    return render(request, 'transactions/finalization_bank.html')

@login_required
def finalization_mortgage(request):
    return render(request, 'transactions/finalization_mortgage.html')

@login_required
def finalization_revision(request):
    contact_name = request.session.get('contact_name')
    contact_email = request.session.get('contact_email')
    contact_address = request.session.get('contact_address')
    contact_zip = request.session.get('contact_zip')
    country = request.session.get('country')
    contact_id = request.session.get('contact_id')
    payment_option = request.session.get('payment_option')

    cardholder_name = request.session.get('cardholder_name')
    card_number = request.session.get('card_number')
    expiry_date = request.session.get('expiry_date')
    cvc = request.session.get('cvc')
    bank_acc = request.session.get('bank_acc')
    provider = request.session.get('provider')

    return render(request, 'transactions/finalization_revision.html', {
        'contact_name': contact_name,
        'contact_email': contact_email,
        'contact_address': contact_address,
        'contact_zip': contact_zip,
        'country': country,
        'contact_id': contact_id,
        'payment_option': payment_option,
        'cardholder_name': cardholder_name,
        'card_number': card_number,
        'expiry_date': expiry_date,
        'cvc': cvc,
        'bank_acc': bank_acc,
        'provider': provider,
    })

@login_required
def finalization_success(request):
    return render(request, 'transactions/finalization_success.html')



'''
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_address = request.POST.get('contact_address')
        contact_zip = request.POST.get('contact_zip')
        country = request.POST.get('country')
        contact_id = request.POST.get('contact_id')
        payment_option = request.POST.get('payment_option')

        cardholder_name = request.POST.get('cardholder_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvc = request.POST.get('cvc')
        bank_acc = request.POST.get('bank-acc')
        provider = request.POST.get('provider')

        request.session['contact_name'] = contact_name
        request.session['contact_email'] = contact_email
        request.session['contact_address'] = contact_address
        request.session['contact_zip'] = contact_zip
        request.session['country'] = country
        request.session['contact_id'] = contact_id
        request.session['payment_option'] = payment_option
        request.session['cardholder_name'] = cardholder_name
        request.session['card_number'] = card_number
        request.session['expiry_date'] = expiry_date
        request.session['cvc'] = cvc
        request.session['bank_acc'] = bank_acc
        request.session['provider'] = provider '''
