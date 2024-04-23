from django.db import models

# Models for the vendor information
class Vendor(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    fax = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    website = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.name}"
