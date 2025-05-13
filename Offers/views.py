
from Offers.forms.create_offer_form import CreateOfferForm
#from Offers.forms.update_offer_form import UpdateOfferForm TODO -------------------
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from Listings.models import Listing
from Buyers.models import Buyer
from Offers.models import Offer

# Create your views here.



# form related views

def create_offer(request,listing_id):

    listing = get_object_or_404(Listing,id=listing_id)

    #buyer = Buyer.objects.get(user=request.user) TODO ----------------
    buyer = Buyer.objects.get(id=1)

    # Skoða hvort til se offer fra buyer fyrir listing
    offer_exists = Offer.objects.filter(
        buyer_id=buyer.id,
        property_listing_id = listing.id
    )
    if offer_exists:
        messages.error(request, 'You have already made an offer for this listing.')
        return redirect('listing-by-id',id=listing.id)
    

    if request.method == "POST":
        form = CreateOfferForm(request.POST)
        

        if form.is_valid():
            messages.success(request, 'Form submission successful')
            offer = form.save(commit=False)
            
            offer.buyer = buyer
            offer.property_listing = listing
            offer.submission_date = timezone.now()
            offer.status = 'PENDING'
            ##offer_image = form.cleaned_data.get('image')
            ##image = OfferImage(image=offer_image, offer=offer)
            ##image.save()
            offer.save()
            return redirect('listing-by-id',id=listing.id)
            ##return redirect('offer-by-id',id = offer.id)
        else:
            messages.error(request, 'Form submission incorrect')
            print(form.errors)
            # Rendera síðu ánþess að missa upplýsingar
            return render(request,'offers/create_offer.html',{"form":form,'listing':listing})
        
    else:
        return render(request, 'offers/create_offer.html',{
            'form': CreateOfferForm(),
            'listing':listing
        })

def delete_offer(request,id):
    offer = get_object_or_404(Offer, id=id)
    offer.delete()
    messages.error(request, 'Offer deleted successfully')
    return redirect('my_offers')

def update_offer(request,id):
    offer = get_object_or_404(Offer,id=id)
    if request.method == 'POST':
        form = CandUpdateForm(request.POST,instance=offer)
        if form.is_valid():
            form.save()
            return redirect(f'offer-by-id',id=offer.id)
    else:
        return render(request, 'offer/update_offer.html', {
            'id': id,
            'form':OfferUpdateForm(instance=offer)
        })