from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Seller
from .forms import SellerProfileForm, CreateSellerForm

# Create your views here.
@login_required
def seller_home(request):
    return render(request, 'seller/base_seller.html')

@login_required
def seller_offers(request):
    return render(request, 'seller/seller_offers.html')

@login_required
def seller_listings(request):
    return render(request, 'seller/manage_listings.html')

@login_required
def seller_add_listing(request):
    return render(request, 'seller/create_listing.html')

@login_required
def seller_edit_listing(request):
    return render(request, 'seller/seller_offers.html')

@login_required
def seller_profile(request):
    user_profile = Seller.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = CreateSellerForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            user_profile.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('seller_profile')
        messages.error(request, 'Please correct the error below.')
        return redirect('seller_profile')

    return render(request, 'seller/seller_profile.html', {
        'form': CreateSellerForm(instance=user_profile)})