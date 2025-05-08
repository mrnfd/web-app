from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to="buyer_profiles/", null=True, blank=True)

    def __str__(self):
        return self.name