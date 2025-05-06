from django.shortcuts import render, get_object_or_404, redirect
from .models import  Buyer
from .forms import BuyerProfileForm

# Create your views here.

def edit_profile(request, buyer_id):
    buyer = get_object_or_404(Buyer, id=buyer_id)

    if request.method == "POST":
        form = BuyerProfileForm(request.POST, request.FILES, instance=buyer)
        if form.is_valid():
            form.save()
            return redirect('profile', buyer_id=buyer_id)
    else:
        form = BuyerProfileForm(instance=buyer)

    return render(request, 'edit_profile.html', {'form': form})
