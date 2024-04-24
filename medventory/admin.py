from django.contrib import admin
from .models import Vendor, Medication, Unit


# Register your models here.
admin.site.register(Vendor)
admin.site.register(Medication)
admin.site.register(Unit)
