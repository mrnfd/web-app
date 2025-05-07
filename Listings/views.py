from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

properties = [
    {
        'id': 1,
        'street': '123 Main St',
        'number': '123',
        'zip': '10001',
    },
    {
        'id': 2,
        'street': '123 Main St',
        'number': '123',
        'zip': '10001',
    },
    {
        'id': 3,
        'street': '123 Main St',
        'number': '123',
        'zip': '10001',
    },
    {
        'id': 4,
        'street': '123 Main St',
        'number': '123',
        'zip': '10001',
    },
]
# Create your views here.

def index(request):
    return render(request,"listing/listings.html",{
        "properties":properties
    })

def get_listing_by_id(request):
    listing = [x for x in properties if x.id == id][0]
    return render(request,"/listings/listing_detail.html.",{
        "listing":listing
    })