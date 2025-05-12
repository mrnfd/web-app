
from Offers.forms.create_offer_form import OfferCreateForm
from Offers.forms.update_offer_form import OfferUpdateForm

from django.shortcuts import render

# Create your views here.



# forms related views

def create_offer(request):
    if request.method == "POST":
        form = OfferCreateForm(request.POST)
        if form.is_valid():
            offer = form.save()
            offer_image = form.cleaned_data.get('image')
            image = OfferImage(image=offer_image, offer=offer)
            image.save()

            return redirect('offer-by-id',id = offer.id)
    else:
        return render(request, 'offer/create_offer.html',{
            'form': OfferCreateForm()
        })

def delete_offer(request,id):
    offer = get_object_or_404(Offer, id=id)
    offer.delete()
    return redirect('offer-index')

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