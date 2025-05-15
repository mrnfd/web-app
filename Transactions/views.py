from Transactions.forms.finalization_form import TransactionForm, CreditCardForm, BankTransferForm, MortgageForm
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from Listings.models import Listing
from Buyers.models import Buyer
from Offers.models import Offer

# Create your views here.
@login_required
def create_offer(request,listing_id):

    listing = get_object_or_404(Listing,id=listing_id)

    buyer = Buyer.objects.get(user=request.user)
    #buyer = Buyer.objects.get(id=1)

    # Skoða hvort til se offer fra buyer fyrir listing
    offer_exists = Offer.objects.filter(
        buyer_id=buyer.id,
        property_listing_id = listing.id
    )
    if offer_exists:
        messages.error(request, 'You have already made an offer for this listing.')
        return redirect('listing-by-id',id=listing.id)
    

    if request.method == "POST":
        form = CreateOfferForm(request.POST)
        

        if form.is_valid():
            messages.success(request, 'Form submission successful')
            offer = form.save(commit=False)
            
            offer.buyer = buyer
            offer.property_listing = listing
            offer.submission_date = timezone.now()
            offer.status = 'PENDING'
            offer.save()
            return redirect('listing-by-id',id=listing.id)
            ##return redirect('offer-by-id',id = offer.id)
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            # Rendera síðu ánþess að missa upplýsingar
            return render(request,'offers/create_offer.html',{"form":form,'listing':listing})
        
    else:
        return render(request, 'offers/create_offer.html',{
            'form': CreateOfferForm(),
            'listing':listing
        })
    

@login_required
def finalization(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Form submission successful')
            contact_info = form.save(commit=False)
            
            contact_info.save()
            return render(request,'transactions/finalize_offer.html',{"form":form})
        
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            # Rendera síðu ánþess að missa upplýsingar
            return render(request,'transactions/finalize_offer.html',{"form":form})
    else:
    
        return render(request, 'transactions/finalize_offer.html',{
            'form': TransactionForm(initial={
                    'contact_email': request.user.email,
                    'contact_name': request.user.buyer.name,
                    'contact_street': request.user.buyer.street,
                    'contact_house_number': request.user.buyer.house_numb,
                    'contact_zip': request.user.buyer.zip_code,
                    'contact_country': request.user.buyer.country,
                }),
        })

@login_required
def finalization_credit(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Form submission successful')
            contact_info = form.save(commit=False)
            
            contact_info.save()
            return render(request,'transactions/finalize_offer.html',{"form":form})
        
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            # Rendera síðu ánþess að missa upplýsingar
            return render(request,'transactions/finalize_offer.html',{"form":form})
    else:
    
        return render(request, 'transactions/finalization_credit.html',{
            'form': TransactionForm(),
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
