from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import  Buyer
from .forms import BuyerProfileForm, CreateBuyerForm
from django.contrib.auth.forms import UserCreationForm
from Offers.models import Offer
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

from Listings.models import Listing, ListingImage
from Sellers.models import Seller


# Create your views here.

def index(request):
    
    return render(request, 'buyers/base_buyer.html')

def register(request):
    if request.method == 'POST':
        form = BuyerProfileForm(request.POST)
        if form.is_valid():

            user = form.save()
            
            try:
                buyer_group = Group.objects.get(name="buyers_group")
                buyer_group.user_set.add(user)
            except Group.DoesNotExist:
                messages.warning(request, 'Buyer group not found. User permissions may be limited.')
            
            buyer = Buyer(
                user=user,
                email=user.email,
                country='Default'  
            )
            buyer.save()
            
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login_as_buyer')
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            return render(request, 'buyers/buyer_register.html', {'form': form})
    else:
        return render(request,'buyers/buyer_register.html', {
            'form': BuyerProfileForm()
        })

# Create your views here.
@login_required
def edit_buyer_profile(request, buyer_id):
    buyer = get_object_or_404(Buyer, id=buyer_id)

    if request.method == "POST":
        form = BuyerProfileForm(request.POST, request.FILES, instance=buyer)
        if form.is_valid():
            form.save()
            buyer.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile', buyer_id=buyer_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = BuyerProfileForm(instance=buyer)
    return render(request, 'edit_buyer_profile.html', {'form': form})



@login_required
def my_offers(request):
    applied_filter = False
    
    try:
        all_offers = Offer.objects.filter(buyer_id=request.user.buyer.id)
            
    except Offer.DoesNotExist:
        return render(request, 'buyers/my_offers.html', {
            "offers": None
        })
    #all_offers = Offer.objects.filter(buyer_id=1)
    #all_offers = Offer.objects.all()
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

        button=''
        if offer.status == 'ACCEPTED':
            button = f'<button data-id = "{offer.id}" type="button" class="finalize-offer-button" >Finalize offer</button>'
        elif offer.status == 'BOUGHT':
            pass
        else:
            button = f'<button data-id = "{offer.id}" type="button" class="edit-offer-button" >Edit offer</button>'
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
            'seller_profile_image_url': listing_seller.profile_image_url,
            'seller_type': listing_seller.seller_type,

            'button': button,
        
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


@login_required
def buyer_catalogue(request):
    return render(request, 'buyers/catalogue.html')

@login_required
def buyer_profile(request):
    user_profile = Buyer.objects.filter(user=request.user).first()
    
    if request.method == 'POST':
        form = CreateBuyerForm(request.POST, request.FILES, instance= user_profile)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            user_profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('buyer_profile')
        messages.error(request, 'Please correct the error below.')
        return redirect('buyer_profile')
        
    return render(request, 'buyers/buyer_profile.html', {
        'form': CreateBuyerForm(instance=user_profile),
    })