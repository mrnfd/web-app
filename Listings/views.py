from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Listings.models import Listing
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
        return JsonResponse({
            'propertys': [{
                'id': property.id,
                'street': property.street,
                'number': property.number,
                'rooms': property.numb_of_rooms,
                'seller': property.seller_id.id,
                'price': str(property.price),
                'thumbnail': property.primary_image(),
                'type': property.type
            } for property in propertys]
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