from django.db import models

# Create your models here.

class Seller(models.Model):
    SELLER_TYPE_CHOICES = [
        ('Individual', 'Individual'),
        ('Agency', 'Real Estate Agency'),
    ]

    #Basic info
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    profile_image_url = models.CharField(max_length=4096, blank=True)

    #seller type
    seller_type = models.CharField(max_length=20, choices=SELLER_TYPE_CHOICES)

    #Address info, only relevant if seller type has 'Agency'
    street = models.CharField(max_length=255, null=True, blank=True)
    house_numb = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=20, null=True, blank=True)

    #Branding image
    logo = models.ImageField(upload_to='seller_logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='seller_cover_images/', blank=True, null=True)

    #Bio description
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name