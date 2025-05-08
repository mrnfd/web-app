from django.db import models
from django.utils import timezone

from Sellers.models import Seller

class PropertyType(models.TextChoices):
    HOUSE = 'HOUSE', 'House'
    CONDO = 'CONDO', 'Condo'
    TOWNHOME = 'TOWNHOME', 'Townhome'
    MULTIFAMILY = 'MULTIFAMILY', 'Multifamily'
    MOBILE = 'MOBILE', 'Mobile'
    FARM = 'FARM', 'Farm'
    LAND = 'LAND', 'Land'
    COMMERCIAL = 'COMMERCIAL', 'Commercial'

class ListingStatus(models.TextChoices):
    PENDING = 'PENDING','Pending'
    ACCEPTED = 'ACCEPTED','Accepted'
    REJECTED = 'REJECTED','Rejected'
    CONTINGENT = 'CONTINGENT','Contingent'

# Create your models here.
class Listing(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE,related_name='images',null=True)

    street = models.CharField(max_length=255,null=True)
    number = models.IntegerField(null=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length =20,choices = PropertyType,default='HOUSE')
    price = models.FloatField(null=True)
    listing_date = models.DateField(default=timezone.now)
    numb_of_rooms = models.IntegerField(null=True)
    size_sqm = models.IntegerField(null=True)
    status = models.CharField(max_length =20,choices = ListingStatus,default = ListingStatus.PENDING)

    def __str__(self):
        return self.title
    
    @property
    def primary_image(self):
        """Returns the first image of the property or None if no images"""
        return self.images.first()

## Getting all offers for a property
#property = PropertyListing.objects.get(id=1)
#all_offers = property.offers.all()  # Returns a QuerySet of all related Offer objects
#
## Getting the count of offers
#offer_count = property.offers.count()
#
## Getting pending offers only
#pending_offers = property.offers.filter(status=OfferStatus.PENDING)

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name='images',null=True)

    image_url =models.CharField(max_length=4096,blank=True)
    thumbnail = models.BooleanField(default=False)
    

