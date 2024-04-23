from django.urls import path
from . import views

urlpatterns = [
    path("vendor/", views.index, name="index"),
    path("vendor/<int:vendor_id>", views.vendor_details, name="vendor_details"),
]
