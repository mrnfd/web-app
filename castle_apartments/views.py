from django.http import HttpResponse
from django.shortcuts import render
from pkg_resources import require


# Create your views here.
def index(request):
    return render(request, 'base.html')

def catalogue(request):
    return render(request, 'catalogue.html')

def sellers(request):
    return render(request, 'sellers.html')

def seller(request, seller_id):
    return render(request, 'seller.html')

def log_in(request):
    return render(request, 'role_selection.html')

def login_as_buyer(request):
    return render(request, 'login.html')

def login_as_seller(request):
    return render(request, 'login.html')
