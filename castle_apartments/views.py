from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from Sellers.models import Seller
from Listings.models import Listing, ListingImage

from django.db.models import Q


# Create your views here.
# Render the base homepage
"""
def index(request):
    return render(request, 'buyers/base_buyer.html')
"""

# Render the catalogue page
def catalogue(request):
    return render(request, 'catalogue.html')

# View to list sellers with optional search filtering
def sellers(request):
    sellers = Seller.objects.all()

    query_params = {
        'search_filter': request.GET.get('search_filter'),
    }

    # If there is a search filter, filter sellers accordingly
    if query_params['search_filter']:
        search_filter = request.GET.get('search_filter', '')
        if search_filter and search_filter != '':
            # Filter sellers based on city, house number, zip code, name or street
            sellers = sellers.filter(
                Q(city__icontains=search_filter) | 
                Q(house_numb__icontains=search_filter) | 
                Q(zip_code__icontains=search_filter) |
                Q(name__icontains=search_filter) |
                Q(street__icontains=search_filter) 
            )
            # Return JSON response
            print("Filters applied, returning JSON response")
            
            
            return JsonResponse({
                'sellers': [{
                    'id': seller.id,
                    'name': seller.name,
                    'seller_type': seller.seller_type,
                    'street': seller.street,
                    'house_numb': seller.house_numb,
                    'city': seller.city,
                    'profile_image_url': seller.profile_image_url
                } for seller in sellers]
            })
            
    # If no filter applied, render the sellers.html template with all sellers
    return render(request, "sellers.html", {
        "sellers": sellers
    })

# View to show details of a single seller and their listed properties
def seller(request, seller_id):
    properties = Listing.objects.filter(seller_id_id=seller_id)
    seller = Seller.objects.get(id=seller_id)

    # Render seller page with seller info and their properties in a dict list
    return render(request, 'seller.html', {
        'seller': seller,
        'properties': [{
                'id': property.id,
                'street': property.street,
                'number': property.number,
                'rooms': property.numb_of_rooms,
                'seller': Seller.objects.get(id = property.seller_id.id).name ,
                'price': str(property.price),
                'thumbnail': property.thumbnail,
                'type': property.type
            } for property in properties]
    })


# Render the role selection page for login
def log_in(request):
    return render(request, 'role_selection.html')

# Render the login page for buyers
def login_as_buyer(request):
    return render(request, 'login.html')

# Render the login page for sellers
def login_as_seller(request):
    return render(request, 'login.html')

# Redirect users after login depending on their group membership
def login_success(request):
    """
    Redirects users based on whether they are in the admins/seller/buyer group
    """
    if request.user.groups.filter(name="admins").exists():
        return redirect("admin_list")
    elif request.user.groups.filter(name="buyers_group").exists():
        # User is a buyer -> redirect to buyer profile page
        return redirect('buyer_profile')
    elif request.user.groups.filter(name="sellers_group").exists():
        # User is a seller -> redirect to seller profile page
        return redirect("seller_profile")
    else:
        # User is in none of the above groups -> redirect to buyer home page as default
        return redirect("buyer_home")