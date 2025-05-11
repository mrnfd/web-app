from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import  Buyer
from .forms import BuyerProfileForm
from django.contrib.auth.forms import UserCreationForm
from Offers.models import Offer
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        print(1)
    else:
        return render(request,'buyers/register.html', {
            'form': UserCreationForm()
        })


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
    return render(request, 'buyers/base_buyer.html')

def buyer_home(request):
    return render(request, 'buyers/base_buyer.html')

def my_offers(request):
    applied_filter = False
    #all_offers = Offer.objects.get(buyer_id=request.user.id)
    #all_offers = Offer.objects.filter(buyer_id = id)
    all_offers = Offer.objects.all()

    query_params = {
        'search_filter': request.GET.get('search_filter'),
        'sort': request.GET.get('sort'),
    }

    if query_params['search_filter']:
        search_filter = request.GET.get('search_filter', '')
        if search_filter and search_filter != '':
            applied_filter = True
            all_offers = all_offers.filter(
                Q(city__icontains=search_filter) | 
                Q(house_numb__icontains=search_filter) | 
                Q(zip_code__icontains=search_filter) |
                Q(name__icontains=search_filter) |
                Q(street__icontains=search_filter) 
            )
            # Return JSON response
            print("Filters applied, returning JSON response")
    # sort by
    sort_options = {
        'price_asc': 'price',
        'price_desc': '-price',
        'street': 'street',
    }
    if query_params['sort'] in sort_options:
        applied_filter = True
        all_offers = all_offers.filter(status= sort_options[query_params['sort']])    

    if applied_filter:        
            return JsonResponse({
                'offers': [{
                    'id': offer.id,
                    'name': offer.name,
                    'seller_type': offer.seller_type,
                    'street': offer.street,
                    'house_numb': offer.house_numb,
                    'city': offer.city,
                    'profile_image_url': offer.profile_image_url
                } for offer in all_offers]
            })
            
    # If no filter return normal
    return render(request, 'buyers/my_offers.html', {
        "offers": all_offers
    })
    

## Getting all offers for a property
#property = PropertyListing.objects.get(id=1)
#all_offers = property.offers.all()  # Returns a QuerySet of all related Offer objects
#
## Getting the count of offers
#offer_count = property.offers.count()
#
## Getting pending offers only
#pending_offers = property.offers.filter(status=OfferStatus.PENDING)

def finalization(request):
    if request.method == "POST":
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_address = request.POST.get('contact_address')
        contact_zip = request.POST.get('contact_zip')
        country = request.POST.get('country')
        contact_id = request.POST.get('contact_id')
        payment_option = request.POST.get('payment_option')

        cardholder_name = request.POST.get('cardholder_name')
        card_number = request.POST.get('card_number')
        expiry_date = request.POST.get('expiry_date')
        cvc = request.POST.get('cvc')
        bank_acc = request.POST.get('bank-acc')
        provider = request.POST.get('provider')

        request.session['contact_name'] = contact_name
        request.session['contact_email'] = contact_email
        request.session['contact_address'] = contact_address
        request.session['contact_zip'] = contact_zip
        request.session['country'] = country
        request.session['contact_id'] = contact_id
        request.session['payment_option'] = payment_option
        request.session['cardholder_name'] = cardholder_name
        request.session['card_number'] = card_number
        request.session['expiry_date'] = expiry_date
        request.session['cvc'] = cvc
        request.session['bank_acc'] = bank_acc
        request.session['provider'] = provider

        return redirect('finalization_revision')

    return render(request, 'buyers/finalize_offer.html')

def finalization_revision(request):
    contact_name = request.session.get('contact_name')
    contact_email = request.session.get('contact_email')
    contact_address = request.session.get('contact_address')
    contact_zip = request.session.get('contact_zip')
    country = request.session.get('country')
    contact_id = request.session.get('contact_id')
    payment_option = request.session.get('payment_option')

    cardholder_name = request.session.get('cardholder_name')
    card_number = request.session.get('card_number')
    expiry_date = request.session.get('expiry_date')
    cvc = request.session.get('cvc')
    bank_acc = request.session.get('bank_acc')
    provider = request.session.get('provider')

    return render(request, 'buyers/finalization_revision.html', {
        'contact_name': contact_name,
        'contact_email': contact_email,
        'contact_address': contact_address,
        'contact_zip': contact_zip,
        'country': country,
        'contact_id': contact_id,
        'payment_option': payment_option,
        'cardholder_name': cardholder_name,
        'card_number': card_number,
        'expiry_date': expiry_date,
        'cvc': cvc,
        'bank_acc': bank_acc,
        'provider': provider,
    })

def finalization_success(request):
    return render(request, 'buyers/finalization_success.html')
def buyer_catalogue(request):
    return render(request, 'buyers/catalogue.html')

def buyer_profile(request):
    return render(request, 'buyers/buyer_profile.html')