from django.utils import timezone
from django.db import models
from Listings.models import Listing
from Buyers.models import Buyer    

# Create your models here.

class OfferStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    ACCEPTED = 'ACCEPTED', 'Accepted'
    REJECTED = 'REJECTED', 'Rejected'
    COUNTERED = 'COUNTERED', 'Countered'

class Offer(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    property_listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    
    price = models.FloatField(null=True)
    submission_date = models.DateField(default=timezone.now)
    expiration_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=OfferStatus.choices, default=OfferStatus.PENDING)
    
    def __str__(self):
        return f"Offer #{self.id} for {self.property_listing.type},{self.property_listing.numb} {self.property_listing.street}"