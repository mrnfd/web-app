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
# Render the main base page
def index(request):
    search_filter = request.GET.get('search_filter')
    if search_filter:
       
        return redirect(f'/catalogue/?search_filter={search_filter}')
    
    return render(request, 'buyers/base_buyer.html')

# User registration view for buyers
def register(request):
    if request.method == 'POST':
        form = BuyerProfileForm(request.POST)
        if form.is_valid():
            # Save new user from registration form
            user = form.save()

            # Try to add the user to the "buyers_group" group
            try:
                buyer_group = Group.objects.get(name="buyers_group")
                buyer_group.user_set.add(user)
            except Group.DoesNotExist:
                # Inform admin or user if group doesn't exist
                messages.warning(request, 'Buyer group not found. User permissions may be limited.')

            # Create a corresponding Buyer instance linked to the User
            buyer = Buyer(
                user=user,
                email=user.email,
                country='Default'  
            )
            buyer.save()
            
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login_as_buyer')
        else:
            # Handle invalid form submission
            messages.error(request, 'Form submission incorrect')
            return render(request, 'buyers/buyer_register.html', {'form': form})
    else:
        # For GET requests, show empty registration form
        return render(request,'buyers/buyer_register.html', {
            'form': BuyerProfileForm()
        })

# Edit buyer profile view - only accessible if logged in
@login_required
def edit_buyer_profile(request, buyer_id):
    # Get buyer or 404 if not found
    buyer = get_object_or_404(Buyer, id=buyer_id)

    if request.method == "POST":
        # Bind form to posted data and files, with existing buyer instance
        form = BuyerProfileForm(request.POST, request.FILES, instance=buyer)
        if form.is_valid():
            form.save() # Save changes to user
            buyer.save() # Save buyer instance
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile', buyer_id=buyer_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        # For GET request, show form prefilled with current buyer data
        form = BuyerProfileForm(instance=buyer)
    return render(request, 'edit_buyer_profile.html', {'form': form})

# View for buyer to see their offers - requires login
@login_required
def my_offers(request):
    applied_filter = False
    
    try:
        # Retrieve all offers made by the current logged-in buyer
        all_offers = Offer.objects.filter(buyer_id=request.user.buyer.id)
    except Offer.DoesNotExist:
        # If no offers, show page with no offers message
        return render(request, 'buyers/my_offers.html', {
            "offers": None
        })

    offer_array = []

    # Get query params from URL for search filter and sort
    query_params = {
        'search_filter': request.GET.get('search_filter'),
        'sort': request.GET.get('sort'),
    }

    # Define valid sorting options for filtering offers by status
    sort_options = {
        'ANY': 'ANY',
        'ACCEPTED': 'ACCEPTED',
        'PENDING': 'PENDING',
        'CONTINGENT': 'CONTINGENT',
        'REJECTED': 'REJECTED'
    }
    # Apply status filter if provided and valid
    if query_params['sort'] and query_params['sort'] in sort_options:
        applied_filter = True
        if query_params['sort'] != 'ANY':
            
            all_offers = all_offers.filter(status=query_params['sort'])

    # Apply search filter (e.g., by street, city, seller name)
    search_filter = request.GET.get('search_filter', '')
    for offer in all_offers:
        offer_listing = Listing.objects.get(id=offer.property_listing_id)
        listing_seller = Seller.objects.get(id=offer_listing.seller_id_id)

        button=''
        # Determine which action button to display based on offer status
        if offer.status == 'ACCEPTED':
            button = f'<button data-id = "{offer.id}" type="button" class="finalize-offer-button" >Finalize offer</button>'
        elif offer.status == 'BOUGHT':
            pass # No button for bought offers
        else:
            button = f'<button data-id = "{offer.id}" type="button" class="edit-offer-button" >Edit offer</button>'

        # Build dictionary with relevant offer + listing + seller info for frontend
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

        # Filter offers by search term if provided
        if search_filter and search_filter != '':
            applied_filter = True
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

    # If filtering applied, return JSON
    if applied_filter:
        return JsonResponse({'offers':offer_array})        
            
    # Otherwise render the normal template with offers
    return render(request, 'buyers/my_offers.html', {
        "offers": offer_array
    })

# Buyer catalogue page
def buyer_catalogue(request):
    return render(request, 'catalogue.html')

# Buyer profile page - allows viewing and editing profile info
@login_required
def buyer_profile(request):
    # Get buyer profile for current logged in user (or None)
    user_profile = Buyer.objects.filter(user=request.user).first()
    
    if request.method == 'POST':
        # Bind form to POST data and files, with existing profile instance
        form = CreateBuyerForm(request.POST, request.FILES, instance= user_profile)
        
        if form.is_valid():
            # Save updated profile and associate with current user
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            user_profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('buyer_profile')
        # On invalid form, display error and redirect back
        messages.error(request, 'Please correct the error below.')
        return redirect('buyer_profile')

    # On GET, display form with existing profile data
    return render(request, 'buyers/buyer_profile.html', {
        'form': CreateBuyerForm(instance=user_profile),
    })