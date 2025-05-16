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
    AVAILABLE = 'AVAILABLE','Available'
    PENDING = 'PENDING','Pending'
    SOLD = 'SOLD','Sold'
    EXPIRED = 'EXPIRED','Expired'
    DELETED = 'DELETED','Deleted'

class City(models.TextChoices):
    NEW_YORK = 'NEW_YORK', 'New York'
    LOS_ANGELES = 'LOS_ANGELES', 'Los Angeles'
    LONDON = 'LONDON', 'London'
    PARIS = 'PARIS', 'Paris'
    BERLIN = 'BERLIN', 'Berlin'
    TOKYO = 'TOKYO', 'Tokyo'
    SEOUL = 'SEOUL', 'Seoul'
    SHANGHAI = 'SHANGHAI', 'Shanghai'
    BEIJING = 'BEIJING', 'Beijing'
    MUMBAI = 'MUMBAI', 'Mumbai'
    DELHI = 'DELHI', 'Delhi'
    SYDNEY = 'SYDNEY', 'Sydney'
    TORONTO = 'TORONTO', 'Toronto'
    VANCOUVER = 'VANCOUVER', 'Vancouver'
    RIO_DE_JANEIRO = 'RIO_DE_JANEIRO', 'Rio de Janeiro'
    MEXICO_CITY = 'MEXICO_CITY', 'Mexico City'
    DUBAI = 'DUBAI', 'Dubai'
    SINGAPORE = 'SINGAPORE', 'Singapore'
    MOSCOW = 'MOSCOW', 'Moscow'
    JOHANNESBURG = 'JOHANNESBURG', 'Johannesburg'
    REYKJAVIK = 'REYKJAVIK', 'Reykjavík'
    ROME = 'ROME', 'Rome'
    BARCELONA = 'BARCELONA', 'Barcelona'
    AMSTERDAM = 'AMSTERDAM', 'Amsterdam'
    BANGKOK = 'BANGKOK', 'Bangkok'
    HONG_KONG = 'HONG_KONG', 'Hong Kong'
    CHICAGO = 'CHICAGO', 'Chicago'
    SAN_FRANCISCO = 'SAN_FRANCISCO', 'San Francisco'
    MIAMI = 'MIAMI', 'Miami'
    CAIRO = 'CAIRO', 'Cairo'

# Create your models here.
class Listing(models.Model):
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE,related_name='seller',null=True)

    street = models.CharField(max_length=255,null=True)
    number = models.IntegerField(null=True)
    zip = models.IntegerField(null=True)
    city = models.CharField(max_length =20,choices = City,null= True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length =20,choices = PropertyType,default='HOUSE')
    price = models.FloatField(null=True)
    listing_date = models.DateField(default=timezone.now)

    numb_of_rooms = models.IntegerField(null=True)
    bath_rooms = models.IntegerField(null=True)
    bed_rooms = models.IntegerField(null=True)

    size_sqm = models.IntegerField(null=True)
    status = models.CharField(max_length =20,choices = ListingStatus,default = ListingStatus.AVAILABLE)

    thumbnail = models.ImageField(upload_to='property_images/',null=True, blank=True)
    
    def __str__(self):
        return self.street
    
    @property
    def primary_image(self):
        """Returns the first image of the property or None if no images"""
        return self.images.first()

class ListingImage(models.Model):
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE,related_name='images',null=True)

    image_url =models.ImageField(upload_to='property_images/',null=True, blank=True)
    thumbnail = models.BooleanField(default=False)
    



