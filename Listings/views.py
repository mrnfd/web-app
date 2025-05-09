from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Listings.models import Listing
from django.db.models import Q

# Create your views here.

# Er að assume-a að listing object heiti Listing




def catalogue(request):
    # Check if filtering is applied
    filter_applied = any(param in request.GET for param in ['search_filter', 'min_price', 'max_price', 'property_type', 'more'])
    propertys = Listing.objects.all()
    
    # Þarf að chekka fyrir hverja tegund af filter

    if 'search_filter' in request.GET:
        search_filter = request.GET.get('search_filter', '')
        if search_filter:
            propertys = propertys.filter(
                #Q(city__icontains=search_filter) | 
                #Q(neighborhood__icontains=search_filter) | 
                #Q(zip__icontains=search_filter) |
                Q(number__icontains=search_filter) |
                Q(street__icontains=search_filter) 
            )

    if 'min_price' in request.GET:
        min_price = request.GET.get('min_price', '')
        if min_price and min_price.strip():
            try:
                propertys = propertys.filter(price__gte=float(min_price))
            except ValueError:
                pass

    if 'max_price' in request.GET:  
        max_price = request.GET.get('max_price', '')
        if max_price and max_price.strip():
            try:
                propertys = propertys.filter(price__lte=float(max_price))
            except ValueError:
                pass  

    if 'property_type' in request.GET:
        property_type = request.GET.get('property_type', '')
        if property_type and property_type != 'any':
            propertys = propertys.filter(property_type=property_type)
    
    if 'more' in request.GET:
        more_filter = request.GET.get('more', '')
        if more_filter:
            if more_filter == '2br':
                propertys = propertys.filter(rooms=2)

    if filter_applied: 
        # Return JSON response
        print("Filters applied, returning JSON response")
        return JsonResponse({
            'propertys': [{
                'id': property.id,
                'street': property.street,
                'number': property.number,
                'rooms': property.numb_of_rooms,
                'seller': property.seller_id.id,
                'price': str(property.price),
                'property_type': property.type
            } for property in propertys.order_by('street')]
        })
    
    # If no filter return normal
    return render(request, "catalogue.html", {
        "propertys": propertys
    })

def get_listing_by_id(request,id):
    listing = Listing.objects.get(id=id)
    #listing = [x for x in propertys if x['id'] == id][0]
    return render(request,"listing_detail.html.",{
        "listing":listing
    })


# Fyrir testing
propertys = [
    {
        'id': 1,
        'street': 'Main St',
        'number': '121',
        'zip': '10001',
        'rooms': '331',
        'seller':'McJohn',
    },
    {
        'id': 2,
        'street': 'Main St',
        'number': '122',
        'zip': '10001',
        'rooms': '332',
        'seller':'McJeff',
    },
    {
        'id': 3,
        'street': 'Main St',
        'number': '123',
        'zip': '10001',
        'rooms': '333',
        'seller':'McClause',
    },
    {
        'id': 4,
        'street': 'Main St',
        'number': '124',
        'zip': '10001',
        'rooms': '334',
        'seller':'McGeorge',
    },
]