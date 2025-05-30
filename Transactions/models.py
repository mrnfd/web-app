from django.db import models

from django.db import models
from django.utils import timezone



from Offers.models import Offer

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

# Create your models here.
class Transaction(models.Model):
    offer = models.OneToOneField(Offer,on_delete=models.CASCADE,related_name='offer')
    finalized = models.BooleanField(default=False)
    
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField(max_length = 254)
    contact_street = models.CharField(max_length=255)
    contact_house_number = models.IntegerField()
    contact_zip = models.IntegerField()
    contact_city = models.CharField(max_length =30,choices = City)
    contact_country = models.CharField(max_length =30,choices = Country)
    contact_SSN = models.CharField(max_length=10)



class PaymentMethodCreditCard(models.Model):
    transaction = models.OneToOneField(Transaction,on_delete=models.CASCADE,related_name='transactionCC')

    contact_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField(blank=True,null=True)
    CVC = models.CharField(max_length=4)

class PaymentMethodBankTransfer(models.Model):
    transaction = models.OneToOneField(Transaction,on_delete=models.CASCADE,related_name='transactionBT')

    bank_account =  models.CharField(max_length=17)

class PaymentMethodMortgage(models.Model):
    transaction = models.OneToOneField(Transaction,on_delete=models.CASCADE,related_name='transactionM')

    mortgage_provider =  models.CharField(max_length=255)