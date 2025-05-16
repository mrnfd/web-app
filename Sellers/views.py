from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Seller
from Listings.models import Listing
from django.contrib.auth.models import Group
from .forms import SellerProfileForm, CreateSellerForm

# Create your views here.
def seller_register(request):
    if request.method == 'POST':
        form = SellerProfileForm(request.POST)
        if form.is_valid():
            # Save new user from registration form
            user = form.save()

            # Try to add the user to the "buyers_group" group
            try:
                seller_group = Group.objects.get(name="sellers_group")
                seller_group.user_set.add(user)
            except Group.DoesNotExist:
                # Inform admin or user if group doesn't exist
                messages.warning(request, 'Seller group not found. User permissions may be limited.')

            # Create a corresponding Buyer instance linked to the User
            buyer = Seller(
                user=user,
                email=user.email,
                country='Default'  
            )
            buyer.save()
            
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login_as_seller')
        else:
            # Handle invalid form submission
            messages.error(request, 'Form submission incorrect')
            return render(request, 'seller/seller_register.html', {'form': form})
    else:
        # For GET requests, show empty registration form
        return render(request,'seller/seller_register.html', {
            'form': SellerProfileForm()
        })

@login_required
def seller_home(request):
    return render(request, 'seller/base_seller.html')

@login_required
def seller_offers(request):
    return render(request, 'seller/seller_offers.html')

@login_required
def seller_listings(request):
    applied_filter = False
    
    try:
        # Retrieve all listings made by the current logged-in buyer
        all_listings = Listing.objects.filter(seller_id_id=request.user.seller.id)
    except Listing.DoesNotExist:
        # If no listings, show page with no offers message
        return render(request, 'seller/manage_listings.html', {
            "offers": None
        })

    listing_array = []

    # Get query params from URL for search filter and sort
    query_params = {
        'search_filter': request.GET.get('search_filter'),
        'sort': request.GET.get('sort'),
    }

    # Define valid sorting options for filtering listings by status
    sort_options = {
        'ANY':'ANY',
        'AVAILABLE': 'AVAILABLE',
        'PENDING': 'PENDING',
        'SOLD': 'SOLD',
        'EXPIRED': 'EXPIRED',
        'DELETED': 'DELETED'
    }
    # Apply status filter if provided and valid
    if query_params['sort'] and query_params['sort'] in sort_options:
        applied_filter = True
        if query_params['sort'] != 'ANY':
            
            all_listings = all_listings.filter(status=query_params['sort'])

    # Apply search filter (e.g., by street, city, seller name)
    search_filter = request.GET.get('search_filter', '')
    for property in all_listings:

        button=''
        # Determine which action button to display based on offer status
        if  property.status == 'PENDING':
            button = f'<button data-id = "{property.id}" type="button" class="finalize-listing-button" >Accept offer</button>'
        elif property.status == 'BOUGHT':
            pass # No button for bought offers
        else:
            button = f'<button data-id = "{property.id}" type="button" class="edit-listing-button" >Edit listing</button>'


        # Build dictionary with relevant offer + listing + seller info for frontend
        listing_info = {
            'id': property.id,
            'street': property.street,
            'number': property.number,
            'rooms': property.numb_of_rooms,
            'seller': Seller.objects.get(id = property.seller_id.id).name ,
            'price': str(property.price),
            'thumbnail': property.thumbnail,
            'type': property.type,
            'status': property.status,

            'button': button,
        }
        # Filter offers by search term if provided
        if search_filter and search_filter != '':
            applied_filter = True
            search_match = (
                search_filter.lower() in property.street.lower() or
                search_filter.lower() in str(property.number).lower() or
                search_filter.lower() in str(property.zip).lower() or
                search_filter.lower() in property.city.lower() or
                search_filter.lower() in property.name.lower()
            )
            if search_match:
                listing_array.append(listing_info)
        else:
            listing_array.append(listing_info)

    # If filtering applied, return JSON
    if applied_filter:
        return JsonResponse({'listings':listing_array})        
            
    # Otherwise render the normal template with offers
    return render(request, 'seller/manage_listings.html', {
        "listings": listing_array
    })

@login_required
def seller_add_listing(request):

    if request.method == "POST":
        form = CreateOfferForm(request.POST)
    else:
        return render(request, 'seller/create_listing.html')

@login_required
def seller_edit_listing(request):
    return render(request, 'seller/seller_offers.html')

@login_required
def seller_profile(request):
    seller = get_object_or_404(Seller, id=request.user.seller.id)
    

    if request.method == "POST":
        form = CreateSellerForm(request.POST, request.FILES, instance=seller)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            seller.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('seller_profile')
        messages.error(request, 'Please correct the error below.')
        return redirect('seller_profile')

    return render(request, 'seller/seller_profile.html', {
        'form': CreateSellerForm(instance=seller)})