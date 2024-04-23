from django.shortcuts import render
from .models import Vendor

# Create your views here.
def index(request):
    vendors = Vendor.objects.all()
    return render(request, "medventory/index.html", {"vendors": vendors})
