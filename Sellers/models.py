from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Country(models.TextChoices):
    UNITED_STATES = 'UNITED_STATES', 'United States'
    CANADA = 'CANADA', 'Canada'
    UNITED_KINGDOM = 'UNITED_KINGDOM', 'United Kingdom'
    GERMANY = 'GERMANY', 'Germany'
    FRANCE = 'FRANCE', 'France'
    ITALY = 'ITALY', 'Italy'
    SPAIN = 'SPAIN', 'Spain'
    NETHERLANDS = 'NETHERLANDS', 'Netherlands'
    SWEDEN = 'SWEDEN', 'Sweden'
    NORWAY = 'NORWAY', 'Norway'
    DENMARK = 'DENMARK', 'Denmark'
    ICELAND = 'ICELAND', 'Iceland'
    AUSTRALIA = 'AUSTRALIA', 'Australia'
    NEW_ZEALAND = 'NEW_ZEALAND', 'New Zealand'
    JAPAN = 'JAPAN', 'Japan'
    SOUTH_KOREA = 'SOUTH_KOREA', 'South Korea'
    CHINA = 'CHINA', 'China'
    INDIA = 'INDIA', 'India'
    BRAZIL = 'BRAZIL', 'Brazil'
    MEXICO = 'MEXICO', 'Mexico'
    RUSSIA = 'RUSSIA', 'Russia'
    SOUTH_AFRICA = 'SOUTH_AFRICA', 'South Africa'
    UNITED_ARAB_EMIRATES = 'UNITED_ARAB_EMIRATES', 'United Arab Emirates'
    SINGAPORE = 'SINGAPORE', 'Singapore'

class Seller(models.Model):
    SELLER_TYPE_CHOICES = [
        ('Individual', 'Individual'),
        ('Agency', 'Real Estate Agency'),
    ]
    user = models.OneToOneField(User,on_delete=models.CASCADE)

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
    country = models.CharField(max_length =30,choices = Country, default='ICELAND')


    #Branding image
    logo = models.ImageField(upload_to='seller_logos/', blank=True, null=True)
    cover_image = models.ImageField(upload_to='seller_cover_images/', blank=True, null=True)

    #Bio description
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name