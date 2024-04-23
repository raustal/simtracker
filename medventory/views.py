from django.shortcuts import render
from .models import Vendor

# Create your views here.
def index(request):
    vendors = Vendor.objects.all()
    return render(request, "medventory/vendor_list.html", {"vendors": vendors})

def vendor_details(request, vendor_id):
    try:
        vendor = Vendor.objects.get(pk=vendor_id)
    except Vendor.DoesNotExist:
        return render(request, "medventory/404.html", {"title": "Vendor Not Found"})
    return render(request, "medventory/vendor_details.html", {"vendor": vendor, "title": "Vendor Details"})
