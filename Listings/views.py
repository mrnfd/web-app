from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Listings.models import Listing, ListingImage
from Sellers.models import Seller
from Buyers.models import Buyer
from Offers.models import Offer

from django.db.models import Q

# Create your views here.

# Er að assume-a að listing object heiti Listing

def catalogue(request):
    # Check if filtering is applied
    filter_applied = any(param in request.GET for param in ['search_filter', 'min_price', 'max_price', 'type', 'more'])
    propertys = Listing.objects.all()

    query_params = {
        'search_filter': request.GET.get('search_filter'),
        'min_price': request.GET.get('min_price'),
        'max_price': request.GET.get('max_price'),
        'type': request.GET.get('type'),
        'more': request.GET.get('more'),
        'sort': request.GET.get('sort'),
    }
    
    # Þarf að chekka fyrir hverja tegund af filter

    if query_params['search_filter']:
        search_filter = request.GET.get('search_filter', '')
        if search_filter and search_filter != '':
            propertys = propertys.filter(
                Q(city__icontains=search_filter) | 
                #Q(neighborhood__icontains=search_filter) | 
                Q(zip__icontains=search_filter) |
                Q(number__icontains=search_filter) |
                Q(street__icontains=search_filter) 
            )

    if query_params['min_price']:
        min_price = request.GET.get('min_price', '')
        if min_price and min_price.strip():
            try:
                propertys = propertys.filter(price__gte=float(min_price))
            except ValueError:
                pass
    
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

    if filter_applied:     
        # Return JSON response
        print("Filters applied, returning JSON response")
        #property_array = []
        #for property in propertys:
        #    property_images = ListingImage.objects.filter(listing_id=property.id)
        #    thumbnail = property_images.filter(thumbnail=True).first()
        #    thumbnail_url = thumbnail.image_url
        #    print("THIS IS MY THUUUUMBNAIAIIAIAL : "+ thumbnail_url)
        #    property_info = {
        #        'id': property.id,
        #        'street': property.street,
        #        'number': property.number,
        #        'rooms': property.numb_of_rooms,
        #        'seller': property.seller_id.id,
        #        'price': str(property.price),
        #        'thumbnail': thumbnail_url,
        #        'type': property.type
        #    }
        #    property_array.append(property_info)
        #return JsonResponse({'propertys':property_array})
        
        return JsonResponse({
            'propertys': [{
                'id': property.id,
                'street': property.street,
                'number': property.number,
                'rooms': property.numb_of_rooms,
                'seller': Seller.objects.get(id = property.seller_id.id).name ,
                'price': str(property.price),
                'thumbnail': property.thumbnail,
                'type': property.type
            } for property in propertys]
        })
    
    # If no filter return normal
    return render(request, "catalogue.html", {
        "propertys": [{
                'id': property.id,
                'street': property.street,
                'number': property.number,
                'rooms': property.numb_of_rooms,
                'seller': Seller.objects.get(id = property.seller_id.id).name ,
                'price': str(property.price),
                'thumbnail': property.thumbnail,
                'type': property.type
            } for property in propertys]
    })

def get_listing_by_id(request,id):

    listing = Listing.objects.get(id=id)
    buyer = None
    
    buyer = Buyer.objects.get(id=1) # TODO   (bara fyrir testing)

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
        button = f'<button data-id = "{{listing.id}}" class="ToCreateOffer-button" > Place a purchase offer</button>'
    elif buyer and offer and listing.status != 'SOLD':
        button = f'<button type="button"  onclick = "redirectToUpdate( {{offer.id}} )"> Edit offer </button>'
    
        


    property_images = ListingImage.objects.filter(listing_id=id)
    seller = Seller.objects.get(id = listing.seller_id.id)

    return render(request,"listing_detail.html",{
        "listing":listing,
        "images":property_images,
        "seller":seller,
        "button":button
    })


# Fyrir testing
#propertys = [
#    {
#        'id': 1,
#        'street': 'Main St',
#        'number': '121',
#        'zip': '10001',
#        'rooms': '331',
#        'seller':'McJohn',
#    },
#    {
#        'id': 2,
#        'street': 'Main St',
#        'number': '122',
#        'zip': '10001',
#        'rooms': '332',
#        'seller':'McJeff',
#    },
#    {
#        'id': 3,
#        'street': 'Main St',
#        'number': '123',
#        'zip': '10001',
#        'rooms': '333',
#        'seller':'McClause',
#    },
#    {
#        'id': 4,
#        'street': 'Main St',
#        'number': '124',
#        'zip': '10001',
#        'rooms': '334',
#        'seller':'McGeorge',
#    },
#]