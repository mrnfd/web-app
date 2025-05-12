from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import  Buyer
from .forms import BuyerProfileForm

# Create your views here.
def edit_buyer_profile(request, buyer_id):
    buyer = get_object_or_404(Buyer, id=buyer_id)

    if request.method == "POST":
        form = BuyerProfileForm(request.POST, request.FILES, instance=buyer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('profile', buyer_id=buyer_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = BuyerProfileForm(instance=buyer)
    return render(request, 'edit_buyer_profile.html', {'form': form})

def index(request):
    return render(request, 'buyers/index.html')

def buyer_home(request):
    return render(request, 'buyers/buyer_home.html')

def buyer_catalogue(request):
    return render(request, 'buyers/catalogue.html')

#Here below is stuff related to authentication
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        return render(request, 'buyer/register.html', {
            'form': UserCreationForm(),
        })

def profile(request):
    return render(request, 'user/profile.html')