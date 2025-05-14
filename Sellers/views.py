from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Seller
from .forms import SellerProfileForm

# Create your views here.
@login_required
def edit_seller_profile(request, seller_id):
    seller = get_object_or_404(Seller, pk=seller_id)

    if request.method == "POST":
        form = SellerProfileForm(request.POST, request.FILES, instance=seller)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully!')
            return redirect('seller_profile', seller_id=seller_id)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SellerProfileForm(instance=seller)
    return render(request, 'edit_seller_profile.html', {'form': form})