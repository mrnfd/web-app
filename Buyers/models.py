from django.contrib.auth.models import User
from django.db import models

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

class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20,null=True,blank=True)
    profile_image_url = models.ImageField(upload_to='images/',null=True, blank=True)
    
    street = models.CharField(max_length=255, null=True, blank=True)
    house_numb = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField(null=True,blank=True)
    country = models.CharField(max_length =30,choices = Country, default='ICELAND')

    def __str__(self):
        return self.name
