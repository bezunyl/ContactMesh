from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True)
    address_country = models.CharField(max_length=100, blank=True)
    address_city = models.CharField(max_length=100, blank=True)
    address_zip = models.CharField('Address ZIP Code', max_length=10, blank=True)
    address_street = models.CharField(max_length=100, blank=True)
    address_aptnum = models.CharField('Address Apartment Number', max_length=10, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    social_instagram = models.URLField(blank=True)
    social_twitter = models.URLField(blank=True)
    social_github = models.URLField(blank=True)
    social_linkedin = models.URLField(blank=True)
    notes = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.get_full_name()
    
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def get_formatted_address(self) -> str:
        return f"{self.address_street} {self.address_aptnum}, {self.address_zip} {self.address_city}, {self.address_country}"
