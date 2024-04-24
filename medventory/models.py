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
    email = models.EmailField(max_length=64)
    website = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.name}"


class Medication(models.Model):
    generic_name = models.CharField(max_length=64)
    trade_name = models.CharField(max_length=64)
    dose = models.FloatField()
    unit = models.ForeignKey("Unit", on_delete=models.CASCADE)
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    item_number = models.CharField(max_length=64)
    barcode = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.generic_name}"


class Unit(models.Model):
    unit = models.CharField(max_length=64)
    unit_abbreviation = models.CharField(max_length=64)

    def __str__(self) -> str:
        return f"{self.unit}"
