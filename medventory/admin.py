from django.contrib import admin
from .models import Vendor, Medication, Unit, TradeName


# Register your models here.
admin.site.register(Vendor)
admin.site.register(Medication)
admin.site.register(Unit)
admin.site.register(TradeName)