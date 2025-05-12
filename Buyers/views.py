from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import  Buyer
from .forms import BuyerProfileForm
from django.contrib.auth.forms import UserCreationForm
from Offers.models import Offer
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

from Listings.models import Listing, ListingImage
from Sellers.models import Seller


# Create your views here.
def index(request):
    return render(request, 'base.html')

def register(request):
    """if request.method == 'POST':
        print(1)
    else:
        return render(request,'buyers/register.html', {
            'form': UserCreationForm()
        })"""
    password = request.POST.get('user_pw')
    confirm_password = request.POST.get('confirm_pw')

    if password != confirm_password:
        messages.error(request, "Passwords do not match.")
        return render(request, "buyers/register.html", {})

    return render(request, "buyers/register.html")

# Create your views here.
def edit_buyer_profile(request, buyer_id):
    buyer = get_object_or_404(Buyer, id=buyer_id)

    if request.method == "POST":
        form = BuyerProfileForm(request.POST, request.FILES, instance=buyer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile', buyer_id=buyer_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = BuyerProfileForm(instance=buyer)
    return render(request, 'edit_buyer_profile.html', {'form': form})

def index(request):
    return render(request, 'buyers/base_buyer.html')

def buyer_home(request):
    return render(request, 'buyers/base_buyer.html')

def my_offers(request):
    applied_filter = False
    #all_offers = Offer.objects.get(buyer_id=request.user.id)
    #all_offers = Offer.objects.filter(buyer_id = id)
    all_offers = Offer.objects.all()
    offer_array = []

    query_params = {
        'search_filter': request.GET.get('search_filter'),
        'sort': request.GET.get('sort'),
    }
            
    # sort by
    sort_options = {
        'ANY': 'ANY',
        'ACCEPTED': 'ACCEPTED',
        'PENDING': 'PENDING',
        'CONTINGENT': 'CONTINGENT',
        'REJECTED': 'REJECTED'
    }
    if query_params['sort'] and query_params['sort'] in sort_options:
        applied_filter = True
        if query_params['sort'] != 'ANY':
            
            all_offers = all_offers.filter(status=query_params['sort'])   

    
    search_filter = request.GET.get('search_filter', '')
    for offer in all_offers:
        offer_listing = Listing.objects.get(id=offer.property_listing_id)
        listing_seller = Seller.objects.get(id=offer_listing.seller_id_id)
        
        offer_info = {
            'id': offer.id,
            'price': str(offer.price),
            'status': offer.status,
            'submission_date':offer.submission_date,
            'expiration_date':offer.expiration_date,

            'listing_id': offer_listing.id,
            'type': offer_listing.type,
            'thumbnail': offer_listing.thumbnail,
            'street': offer_listing.street,
            'number': offer_listing.number,
            'zip': offer_listing.zip,
            'city': offer_listing.city,
            
            'seller': listing_seller.name,
            'seller_id': listing_seller.id,
        
        }
        
        if search_filter and search_filter != '':
            
            applied_filter = True
                       
            #if search_filter in offer_info['street'] or search_filter in offer_info['number'] or search_filter in offer_info['zip'] or search_filter in offer_info['city']:
            #    offer_array.append(offer_info) 
            search_match = (
                search_filter.lower() in offer_listing.street.lower() or
                search_filter.lower() in str(offer_listing.number).lower() or
                search_filter.lower() in str(offer_listing.zip).lower() or
                search_filter.lower() in offer_listing.city.lower() or
                search_filter.lower() in listing_seller.name.lower()
            )
            
            if search_match:
                offer_array.append(offer_info)
        else:
            offer_array.append(offer_info)

    print(applied_filter)
    if applied_filter:
        return JsonResponse({'offers':offer_array})        
            
    # If no filter return normal
    return render(request, 'buyers/my_offers.html', {
        "offers": offer_array
    })
    

## Getting all offers for a property
#property = PropertyListing.objects.get(id=1)
#all_offers = property.offers.all()  # Returns a QuerySet of all related Offer objects
#
## Getting the count of offers
#offer_count = property.offers.count()
#
## Getting pending offers only
#pending_offers = property.offers.filter(status=OfferStatus.PENDING)

def finalization(request):
    if request.method == "POST":
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
        request.session['provider'] = provider

        return redirect('finalization_revision')

    return render(request, 'buyers/finalize_offer.html')

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

    return render(request, 'buyers/finalization_revision.html', {
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

def finalization_success(request):
    return render(request, 'buyers/finalization_success.html')
def buyer_catalogue(request):
    return render(request, 'buyers/catalogue.html')

def buyer_profile(request):
    return render(request, 'buyers/buyer_profile.html')