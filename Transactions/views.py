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
            for field in form.fields.values():
                field.disabled = False
        except Transaction.DoesNotExist:
            form = TransactionForm(request.POST)
        
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.offer_id = offer.id
            transaction.save()  # Save to generate an ID

            # Determine selected payment option and redirect accordingly
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
            # Form is invalid; show error and render form again
            messages.error(request, 'Please correct the errors in the form.')
            return render(request, 'transactions/finalize_offer.html', {
                "form": form, 
                'offer': offer,
                'transaction_id': None
            })
    else:
        try:
            transaction = Transaction.objects.get(offer=offer)
            if not transaction.finalized:
                form = TransactionForm(instance=transaction)
            else:
                # Prevent editing of finalized transaction
                messages.error(request, 'Error has occurred the property is currently not available.')
                return redirect('my_offers') 
        except Transaction.DoesNotExist:
            # Prefill form with user info if no transaction exists yet
            form = TransactionForm(initial={
            'contact_email': request.user.email,
            'contact_name': request.user.buyer.name,
            'contact_street': request.user.buyer.street,
            'contact_house_number': request.user.buyer.house_numb,
            'contact_zip': request.user.buyer.zip_code,
            'contact_country': request.user.buyer.country,
            })

        return render(request, 'transactions/finalize_offer.html', {
            'form': form,
            'offer': offer,
            'transaction_id': None,
        })

@login_required
def finalization_credit(request,transaction_id):
    transactionX=get_object_or_404(Transaction,id=transaction_id)
    if request.method == "POST":
        try:
            transactionCC = PaymentMethodCreditCard.objects.get(transaction=transactionX)
            form = CreditCardForm(request.POST,instance=transactionCC)
        except PaymentMethodCreditCard.DoesNotExist:
            form = CreditCardForm(request.POST)

        if form.is_valid():
            payment_info = form.save(commit=False)
            payment_info.transaction = transactionX
            payment_info.save()
            return redirect('finalization_revision', transactionX.id,'creditcard')
        else:
            messages.error(request, 'Form submission incorrect')
            return render(request,'transactions/finalization_credit.html',{
                "form":form,
                'transaction':transactionX,})
    else:
        try:
            transactionCC = PaymentMethodCreditCard.objects.get(transaction=transactionX)
            form = CreditCardForm(instance=transactionCC)
            for field in form.fields.values():
                field.disabled = False # Allow editing existing values
        except PaymentMethodCreditCard.DoesNotExist:
            form = CreditCardForm()
        
    
        return render(request, 'transactions/finalization_credit.html',{
            'form': form,
            'transaction':transactionX,
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
            return redirect('finalization_revision', transaction.id,'banktransfer')
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            return render(request,'transactions/finalization_bank.html',{
                "form":form,
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
            return redirect('finalization_revision', transaction.id,'mortgage')
        
        else:
            messages.error(request, 'Form submission incorrect')
            return render(request,'transactions/finalization_mortgage.html',{
                "form":form,
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
def finalization_revision(request,transaction_id,paymentmethod):
    transaction=get_object_or_404(Transaction,id=transaction_id)

    if request.method == "POST":
        return redirect('finalization_success', transaction.id)
    
    else:
        form1 = TransactionForm(instance=transaction)
        paymenttype = ''
        # Load corresponding payment form based on method
        if paymentmethod == 'creditcard':
            paymenttype = 'transactionCC'
            form2 = CreditCardForm(instance=transaction.transactionCC)
        elif paymentmethod == 'banktransfer':
            paymenttype = 'transactionBT'
            form2 = BankTransferForm(instance=transaction.transactionBT)
        elif paymentmethod == 'mortgage':
            paymenttype = 'transactionM'
            form2 = MortgageForm(instance=transaction.transactionM)

        # Make all fields readonly
        for field in form1.fields.values():
                field.disabled = True
        for field in form2.fields.values():
                field.disabled = True

        return render(request, 'transactions/finalization_revision.html', {
            'form1':form1,
            'form2':form2,
            'transaction':transaction,
            'paymentmethod':paymenttype
        })

@login_required
def finalization_success(request,transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.finalized = True
    offer = transaction.offer
    offer.status = 'BOUGHT' # Update status to show it has been purchased
    offer.save()
    transaction.save()
    return render(request, 'transactions/finalization_success.html',{'transaction_id':transaction_id})

@login_required
def delete_transaction(request,transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.delete()
    return redirect('my_offers')