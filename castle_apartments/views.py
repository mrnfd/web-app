from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from Sellers.models import Seller
from Listings.models import Listing, ListingImage

from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'base.html')

def catalogue(request):
    return render(request, 'catalogue.html')

def sellers(request):
    sellers = Seller.objects.all()

    query_params = {
        'search_filter': request.GET.get('search_filter'),
    }

    if query_params['search_filter']:
        search_filter = request.GET.get('search_filter', '')
        if search_filter and search_filter != '':
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
            
    # If no filter return normal
    return render(request, "sellers.html", {
        "sellers": sellers
    })


def seller(request, seller_id):
    properties = Listing.objects.filter(seller_id_id=seller_id)
    seller = Seller.objects.get(id=seller_id)

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


## Getting all offers for a property
#property = PropertyListing.objects.get(id=1)
#all_offers = property.offers.all()  # Returns a QuerySet of all related Offer objects
#
## Getting the count of offers
#offer_count = property.offers.count()
#
## Getting pending offers only
#pending_offers = property.offers.filter(status=OfferStatus.PENDING)

def log_in(request):
    return render(request, 'role_selection.html')

def login_as_buyer(request):
    return render(request, 'login.html')

def login_as_seller(request):
    return render(request, 'login.html')

def login_success(request):
    """
    Redirects users based on whether they are in the admins/seller/buyer group
    """
    if request.user.groups.filter(name="admins").exists():
        # user is an admin
        return redirect("admin_list")
    elif request.user.groups.filter(name="buyers_group").exists():
        return redirect('buyer_profile')
    elif request.user.groups.filter(name="sellers_group").exists():
        return redirect("buyer_profile")
    else:
        return redirect("buyer_home")