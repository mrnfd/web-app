from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    profile_image_url = models.CharField(max_length=4096, blank = True)
    
    street = models.CharField(max_length=255, null=True, blank=True)
    house_numb = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name