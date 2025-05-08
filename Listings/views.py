from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from Listings.models import Listing

# Create your views here.

# Er að assume-a að listing object heiti Listing

def catalogue(request):
    #if 'search_filter' in request.GET:
    #    return JsonResponse({
    #          'data':[{
    #                
    #          } for x in Listing.objects.filter(name__icontains=request.GET['search_filter'].order_by('name'))]
    #    })
    #
    propertys = Listing.objects.all()
    return render(request,"catalogue.html",{
        "propertys":propertys
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