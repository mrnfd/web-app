from Transactions.forms.finalization_form import TransactionForm, CreditCardForm, BankTransferForm, MortgageForm
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from Listings.models import Listing
from Buyers.models import Buyer
from Offers.models import Offer
from Transactions.models import Transaction, PaymentMethodCreditCard, PaymentMethodBankTransfer, PaymentMethodMortgage
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
                    'offer': offer,
                    'transaction_id': transaction.id
                })
        else:
            print("Form is invalid")  # Debug print
            print(f"Form errors: {form.errors}")  # Debug print to see validation errors
            messages.error(request, 'Please correct the errors in the form.')
            return render(request, 'transactions/finalize_offer.html', {
                "form": form, 
                'offer': offer,
                'transaction_id': None
            })
    else:

        try:
            transaction = Transaction.objects.get(offer=offer)
            form = TransactionForm(instance=transaction)
            for field in form.fields.values():
                field.disabled = False
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
            'offer': offer,
            'transaction_id': None,
        })

@login_required
def finalization_credit(request,transaction_id):
    transaction=get_object_or_404(Transaction,id=transaction_id)
    if request.method == "POST":

        try:
            transactionCC = PaymentMethodCreditCard.objects.get(transaction=transaction_id)
            form = CreditCardForm(request.POST,instance=transactionCC)
        except PaymentMethodCreditCard.DoesNotExist:
            form = CreditCardForm(request.POST)

        if form.is_valid():

            payment_info = form.save(commit=False)
            payment_info.transaction = transaction
            
            payment_info.save()
            return redirect('finalization_revision', transaction.id)
            #return render(request,'transactions/finalization_credit.html',{
            #    'form':form,
            #    'transaction':transaction,
            #    })
        
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            
            # Rendera síðu ánþess að missa upplýsingar
            return render(request,'transactions/finalization_credit.html',{"form":form,
                                                                           'transaction':transaction,})
    else:
        try:
            transactionCC = PaymentMethodCreditCard.objects.get(transaction=transaction_id)
            form = CreditCardForm(instance=transactionCC)
            for field in form.fields.values():
                field.disabled = False
        except PaymentMethodCreditCard.DoesNotExist:
            form = CreditCardForm()
        
    
        return render(request, 'transactions/finalization_credit.html',{
            'form': form,
            'transaction':transaction,
        })
   

@login_required
def finalization_bank(request,transaction_id):
    transaction=get_object_or_404(Transaction,id=transaction_id)
    if request.method == "POST":

        try:
            transactionBT = PaymentMethodBankTransfer.objects.get(transaction=transaction_id)
            form = BankTransferForm(request.POST,instance=transactionBT)
        except PaymentMethodBankTransfer.DoesNotExist:
            form = BankTransferForm(request.POST)

        if form.is_valid():

            payment_info = form.save(commit=False)
            payment_info.transaction = transaction
            
            payment_info.save()
            return redirect('finalization_revision', transaction.id)
            
        
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            
            # Rendera síðu ánþess að missa upplýsingar
            return render(request,'transactions/finalization_bank.html',{"form":form,
                                                                           'transaction':transaction,})
    else:
        try:
            transactionBT = PaymentMethodBankTransfer.objects.get(transaction=transaction_id)
            form = BankTransferForm(instance=transactionBT)
            for field in form.fields.values():
                field.disabled = False
        except PaymentMethodBankTransfer.DoesNotExist:
            form = BankTransferForm()
        
    
        return render(request, 'transactions/finalization_bank.html',{
            'form': form,
            'transaction':transaction,
        })
    

@login_required
def finalization_mortgage(request,transaction_id):
    transaction=get_object_or_404(Transaction,id=transaction_id)
    if request.method == "POST":

        try:
            transactionM = PaymentMethodMortgage.objects.get(transaction=transaction_id)
            form = MortgageForm(request.POST,instance=transactionM)
        except PaymentMethodMortgage.DoesNotExist:
            form = MortgageForm(request.POST)

        if form.is_valid():

            payment_info = form.save(commit=False)
            payment_info.transaction = transaction
            
            payment_info.save()
            return redirect('finalization_revision', transaction.id)
        
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            
            # Rendera síðu ánþess að missa upplýsingar
            return render(request,'transactions/finalization_mortgage.html',{"form":form,
                                                                           'transaction':transaction,})
    else:
        try:
            transactionM = PaymentMethodMortgage.objects.get(transaction=transaction_id)
            form = MortgageForm(instance=transactionM)
            for field in form.fields.values():
                field.disabled = False
        except PaymentMethodMortgage.DoesNotExist:
            form = MortgageForm()
        
    
        return render(request, 'transactions/finalization_mortgage.html',{
            'form': form,
            'transaction':transaction,
        })
    

@login_required
def finalization_revision(request,transaction_id):
    transaction=get_object_or_404(Transaction,id=transaction_id)

    form1 = TransactionForm(instance=transaction)
    
    paymentmethod = ''
    if hasattr(transaction, 'transactionCC'):
        paymentmethod = 'transactionCC'
        form2 = CreditCardForm(instance=transaction.transactionCC)
    elif hasattr(transaction, 'transactionBT'):
        paymentmethod = 'transactionBT'
        form2 = BankTransferForm(instance=transaction.transactionBT)
    elif hasattr(transaction, 'transactionM'):
        paymentmethod = 'transactionM'
        form2 = MortgageForm(instance=transaction.transactionM)

    # Gera form readonly
    for field in form1.fields.values():
            field.disabled = True
    for field in form2.fields.values():
            field.disabled = True

    return render(request, 'transactions/finalization_revision.html', {
        'form1':form1,
        'form2':form2,
        'transaction':transaction,
        'paymentmethod':paymentmethod
    })

@login_required
def finalization_success(request,transaction_id):
    return render(request, 'transactions/finalization_success.html',{'transaction_id':transaction_id})

@login_required
def delete_transaction(request,transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.delete()
    
    return redirect('my_offers')


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
