from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'base.html')

def catalogue(request):
    return render(request, 'catalogue.html')



def sellers(request):
    return HttpResponse("sellers page")

def my_offers(request):
    return HttpResponse("log in to see your offers")

def log_in(request):
    return render(request, 'role_selection.html')

def login_as_buyer(request):
    return HttpResponse("log in as buyer page")

def login_as_seller(request):
    return HttpResponse("log in as seller page")
