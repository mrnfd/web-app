from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from Sellers.models import Seller

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
    return render(request, 'seller.html')

def log_in(request):
    return render(request, 'role_selection.html')

def login_as_buyer(request):
    return render(request, 'login.html')

def login_as_seller(request):
    return render(request, 'login.html')
