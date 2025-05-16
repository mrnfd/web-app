from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Listings.models import Listing, ListingImage
from Sellers.models import Seller
from Buyers.models import Buyer
from Offers.models import Offer

from django.db.models import Q

# Create your views here.
# Assumes that the listing model is named Listing

def catalogue(request):
    # Check if any filtering parameters are present in the GET request
    filter_applied = any(param in request.GET for param in ['search_filter', 'min_price', 'max_price', 'type', 'more'])
    # Start with all listings
    propertys = Listing.objects.all()

    # Extract possible query parameters from GET request
    query_params = {
        'search_filter': request.GET.get('search_filter'),
        'min_price': request.GET.get('min_price'),
        'max_price': request.GET.get('max_price'),
        'type': request.GET.get('type'),
        'more': request.GET.get('more'),
        'sort': request.GET.get('sort'),
    }

    # Apply search filter: search across city, zip, number, and street fields (case-insensitive)
    if query_params['search_filter']:
        search_filter = request.GET.get('search_filter', '')
        if search_filter and search_filter != '':
            propertys = propertys.filter(
                Q(city__icontains=search_filter) |
                Q(zip__icontains=search_filter) |
                Q(number__icontains=search_filter) |
                Q(street__icontains=search_filter) 
            )

    # Filter by minimum price if valid
    if query_params['min_price']:
        min_price = request.GET.get('min_price', '')
        if min_price and min_price.strip():
            try:
                propertys = propertys.filter(price__gte=float(min_price))
            except ValueError:
                # Ignore invalid min_price values (non-numeric)
                pass

    # Filter by maximum price if valid
    if query_params['max_price']:
        max_price = request.GET.get('max_price', '')
        if max_price and max_price.strip():
            try:
                propertys = propertys.filter(price__lte=float(max_price))
            except ValueError:
                pass
             
    if query_params['type']:
        type = request.GET.get('type', '')
        if type and type != 'ANY':
            propertys = propertys.filter(type=type)
    
    if query_params['more']:
        more_filter = request.GET.get('more', '')
        if more_filter:
            if more_filter == '2br':
                propertys = propertys.filter(rooms=2)

    # sort by
    sort_options = {
        'price_asc': 'price',
        'price_desc': '-price',
        'street': 'street',
    }
    if query_params['sort'] in sort_options:
        propertys = propertys.order_by(sort_options[query_params['sort']])

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'propertys': [{
                'id': property.id,
                'street': property.street,
                'number': property.number,
                'rooms': property.numb_of_rooms,
                'seller': Seller.objects.get(id=property.seller_id.id).name,
                'price': str(property.price),
                'thumbnail': property.thumbnail,
                'type': property.type,
                'status': property.status
            } for property in propertys]
        })
        
    return render(request, "catalogue.html", {
        "propertys": [{
                'id': property.id,
                'street': property.street,
                'number': property.number,
                'rooms': property.numb_of_rooms,
                'seller': Seller.objects.get(id = property.seller_id.id).name ,
                'price': str(property.price),
                'thumbnail': property.thumbnail,
                'type': property.type,
                'status': property.status
            } for property in propertys]
    })

def get_listing_by_id(request,id):

    listing = Listing.objects.get(id=id)
    buyer = None
    #buyer = Buyer.objects.get(user=request.user)
    #buyer = Buyer.objects.get(id=1) # TODO   (bara fyrir testing)

    if request.user.is_authenticated:
        try:
            buyer = Buyer.objects.get(user=request.user) 
            
        except Buyer.DoesNotExist:
            pass
    
    # Skoða hvort offer sé til
    offer = None
    if buyer:
        try:
            offer = Offer.objects.get(
                buyer_id=buyer.id,
                property_listing_id=listing.id
            )
        except Offer.DoesNotExist:
            pass
    
    button=''
    if buyer and listing.status != 'SOLD' and not offer:
        button = f'<button data-id = "{listing.id}" class="create-offer-button" > Place a purchase offer</button>'
    elif buyer and offer and listing.status != 'SOLD':
        
        button = f'<button data-id = "{offer.id}" class="update-offer-button" > Edit offer</button>'
        #button = f'<button type="button"  onclick = "redirectToUpdate( {{offer.id}} )"> Edit offer </button>'

    property_images = ListingImage.objects.filter(listing_id=id)
    seller = Seller.objects.get(id = listing.seller_id.id)

    return render(request,"listing_detail.html",{
        "listing":listing,
        "images":property_images,
        "seller":seller,
        "button":button
    })